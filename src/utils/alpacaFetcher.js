import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const ALPACA_API_URL = 'https://data.alpaca.markets/v1beta3/crypto';
const ALPACA_API_KEY = process.env.ALPACA_API_KEY;
const ALPACA_SECRET_KEY = process.env.ALPACA_SECRET_KEY;

/**
 * Fetch historical bars for a list of crypto symbols between specified dates.
 * Endpoint: GET /v1beta3/crypto/{loc}/bars
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch historical bars for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @param {string} startDate - The start date for historical data in YYYY-MM-DD format.
 * @param {string} endDate - The end date for historical data in YYYY-MM-DD format.
 * @returns {Object|null} - Historical bars data or null in case of error.
 */
async function fetchHistoricalBars(symbols, loc, startDate, endDate) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/bars`, {
      params: {
        symbols: symbols,
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

/**
 * Fetch the latest bars for a list of crypto symbols.
 * Endpoint: GET /v1beta3/crypto/{loc}/latest/bars
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch latest bars for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @returns {Object|null} - Latest bars data or null in case of error.
 */
async function fetchLatestBars(symbols, loc) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/latest/bars`, {
      params: {
        symbols: symbols,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the latest bars data
  } catch (error) {
    console.error(`Error fetching latest bars: ${error.message}`);
    return null; // Return null in case of error
  }
}

/**
 * Fetch the latest order book for a list of crypto symbols.
 * Endpoint: GET /v1beta3/crypto/{loc}/latest/orderbooks
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch the latest order book for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @returns {Object|null} - Latest order book data or null in case of error.
 */
async function fetchLatestOrderBook(symbols, loc) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/latest/orderbooks`, {
      params: {
        symbols: symbols,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the latest order book data
  } catch (error) {
    console.error(`Error fetching latest order book: ${error.message}`);
    return null; // Return null in case of error
  }
}

/**
 * Fetch the latest quotes for a list of crypto symbols.
 * Endpoint: GET /v1beta3/crypto/{loc}/latest/quotes
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch the latest quotes for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @returns {Object|null} - Latest quotes data or null in case of error.
 */
async function fetchLatestQuotes(symbols, loc) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/latest/quotes`, {
      params: {
        symbols: symbols,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the latest quotes data
  } catch (error) {
    console.error(`Error fetching latest quotes: ${error.message}`);
    return null; // Return null in case of error
  }
}

/**
 * Fetch the latest trades for a list of crypto symbols.
 * Endpoint: GET /v1beta3/crypto/{loc}/latest/trades
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch the latest trades for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @returns {Object|null} - Latest trades data or null in case of error.
 */
async function fetchLatestTrades(symbols, loc) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/latest/trades`, {
      params: {
        symbols: symbols,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the latest trades data
  } catch (error) {
    console.error(`Error fetching latest trades: ${error.message}`);
    return null; // Return null in case of error
  }
}

/**
 * Fetch historical quotes for a list of crypto symbols between specified dates.
 * Endpoint: GET /v1beta3/crypto/{loc}/quotes
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch historical quotes for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @param {string} startDate - The start date for historical data in YYYY-MM-DD format.
 * @param {string} endDate - The end date for historical data in YYYY-MM-DD format.
 * @returns {Object|null} - Historical quotes data or null in case of error.
 */
async function fetchHistoricalQuotes(symbols, loc, startDate, endDate) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/quotes`, {
      params: {
        symbols: symbols,
        start: startDate,
        end: endDate,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the historical quotes data
  } catch (error) {
    console.error(`Error fetching historical quotes: ${error.message}`);
    return null; // Return null in case of error
  }
}

/**
 * Fetch snapshots for a list of crypto symbols.
 * Endpoint: GET /v1beta3/crypto/{loc}/snapshots
 * 
 * @param {string} symbols - Comma-separated list of crypto symbols to fetch snapshots for.
 * @param {string} loc - The location (exchange) to fetch data from (e.g., 'binance').
 * @returns {Object|null} - Snapshots data or null in case of error.
 */
async function fetchSnapshots(symbols, loc) {
  try {
    const response = await axios.get(`${ALPACA_API_URL}/${loc}/snapshots`, {
      params: {
        symbols: symbols,
      },
      headers: {
        'APCA_API_KEY_ID': ALPACA_API_KEY,
        'APCA_API_SECRET_KEY': ALPACA_SECRET_KEY,
      },
    });

    return response.data; // Return the snapshots data
  } catch (error) {
    console.error(`Error fetching snapshots: ${error.message}`);
    return null; // Return null in case of error
  }
}

export { 
  fetchHistoricalBars, 
  fetchLatestBars, 
  fetchLatestOrderBook, 
  fetchLatestQuotes, 
  fetchLatestTrades, 
  fetchHistoricalQuotes, 
  fetchSnapshots 
};