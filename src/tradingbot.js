import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const ALPACA_API_URL = 'https://data.alpaca.markets/v1beta3/crypto';
const ALPACA_API_KEY = process.env.ALPACA_API_KEY;
const ALPACA_SECRET_KEY = process.env.ALPACA_SECRET_KEY;

async function fetchHistoricalBars(symbol, loc, startDate, endDate) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/bars`, {
      params: {
        symbols: symbol,
        start: startDate,
        end: endDate,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the historical bars data
  } catch (error) {
    console.error(`Error fetching historical bars: ${error.message}`);
    return null; // Return null in case of error
  }
}

export { fetchHistoricalBars };
