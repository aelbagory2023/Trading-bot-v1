import axios from 'axios';

const COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/coins/markets';
const BASE_CURRENCY = 'usd'; // You can change this to your preferred currency

async function fetchTokenAddresses() {
  try {
    const response = await axios.get(COINGECKO_API_URL, {
      params: {
        vs_currency: BASE_CURRENCY,
        order: 'market_cap_desc',
        per_page: 100, // Adjust the number of tokens to fetch
        page: 1,
        sparkline: false,
      },
    });

    const tokens = response.data.map(token => ({
      id: token.id, // CoinGecko ID
      symbol: token.symbol, // Token symbol
      name: token.name, // Token name
      address: token.platforms?.ethereum || null, // Fetching Ethereum address
    })).filter(token => token.address); // Filter out tokens without an address

    return tokens;
  } catch (error) {
    console.error(`Error fetching token addresses: ${error.message}`);
    return [];
  }
}

export { fetchTokenAddresses };
