import { fetchTokenAddresses } from "./utils/tokenFetcher.js";
import {
  fetchHistoricalBars,
  fetchLatestBars,
  fetchLatestOrderBook,
  fetchLatestQuotes,
  fetchLatestTrades,
  fetchHistoricalQuotes,
  fetchHistoricalTrades,
  fetchSnapshots,
} from "./utils/alpacaFetcher.js";

async function getTradingSignal() {
  const tokens = await fetchTokenAddresses();

  // Example logic to determine which token to trade
  const selectedToken = tokens[0]; // Select the first token for demonstration

  // Fetch historical bars for the selected token
  const loc = "binance"; // Example location, adjust as needed
  const startDate = "2023-01-01"; // Example start date
  const endDate = "2023-12-31"; // Example end date
  const historicalBars = await fetchHistoricalBars(
    selectedToken.symbol,
    loc,
    startDate,
    endDate
  );

  console.log("Historical Bars:", historicalBars); // Log the historical bars data

  // Fetch latest bars for the selected token
  const latestBars = await fetchLatestBars(selectedToken.symbol, loc);
  console.log("Latest Bars:", latestBars); // Log the latest bars data

  // Fetch latest order book for the selected token
  const latestOrderBook = await fetchLatestOrderBook(selectedToken.symbol, loc);
  console.log("Latest Order Book:", latestOrderBook); // Log the latest order book data

  // Fetch latest quotes for the selected token
  const latestQuotes = await fetchLatestQuotes(selectedToken.symbol, loc);
  console.log("Latest Quotes:", latestQuotes); // Log the latest quotes data

  // Fetch latest trades for the selected token
  const latestTrades = await fetchLatestTrades(selectedToken.symbol, loc);
  console.log("Latest Trades:", latestTrades); // Log the latest trades data

  // Fetch historical quotes for the selected token
  const historicalQuotes = await fetchHistoricalQuotes(
    selectedToken.symbol,
    loc,
    startDate,
    endDate
  );
  console.log("Historical Quotes:", historicalQuotes); // Log the historical quotes data

  // Fetch historical trades for the selected token
  const historicalTrades = await fetchHistoricalTrades(
    selectedToken.symbol,
    loc,
    startDate,
    endDate
  );
  console.log("Historical Trades:", historicalTrades); // Log the historical trades data

  return {
    action: "buy", // or 'sell'
    token: selectedToken.address,
    amount: "0.001", // Example amount
  };
}

export { getTradingSignal };
