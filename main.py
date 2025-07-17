import os
import json
from telegram.ext import ApplicationBuilder, CommandHandler

# Load rarity rank data
with open("rarity_ranks.json", "r") as f:
    id_to_rank = json.load(f)

TOTAL_NFTS = 10000  # Adjust if needed

# Get bot token from environment variable
# TOKEN = os.getenv("7763462069:AAGGX-_VFKLfqe-xqEytL7dXLfKHo1Ozj2A")

# /start command
async def start(update, context):
    await update.message.reply_text("👋 Hi! Use /rarity <id> to check NFT rarity rank.")

# /rarity command
async def rarity(update, context):
    try:
        nft_id = int(context.args[0])
        rank = id_to_rank.get(str(nft_id))
        if rank:
            await update.message.reply_text(f"Rarity rank: {rank}/{TOTAL_NFTS}")
        else:
            await update.message.reply_text("❌ NFT ID not found.")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /rarity <id>")

# Main function
def main():
    app = ApplicationBuilder().token("7763462069:AAGGX-_VFKLfqe-xqEytL7dXLfKHo1Ozj2A").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rarity", rarity))
    app.run_polling()

if __name__ == "__main__":
    main()