#!/bin/bash

# Define colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

COOKIE_FILE="youtube_cookies.txt"

echo -e "${YELLOW}🍪 YouTube Cookie Setup Helper${NC}"
echo "========================================"

# Check if cookie file exists
if [ ! -f "$COOKIE_FILE" ]; then
    echo -e "${RED}❌ Error: $COOKIE_FILE not found!${NC}"
    echo "Please place your youtube_cookies.txt in the current directory."
    exit 1
fi

# Encode cookies to base64
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    ENCODED_COOKIES=$(cat "$COOKIE_FILE" | base64)
else
    # Linux/Windows
    ENCODED_COOKIES=$(cat "$COOKIE_FILE" | base64 -w 0)
fi

echo -e "${GREEN}✅ Cookies encoded successfully!${NC}"
echo ""
echo "--------------------------------------------------"
echo "$ENCODED_COOKIES"
echo "--------------------------------------------------"
echo ""
echo "📝 INSTRUCTIONS:"
echo "1. Copy the alphanumeric text between the dashed lines above."
echo "2. Go to your GitHub Repository Settings -> Secrets -> Actions."
echo "3. Create a new repository secret named: ${GREEN}YOUTUBE_COOKIES_BASE64${NC}"
echo "4. Paste the copied text as the value."
echo ""
