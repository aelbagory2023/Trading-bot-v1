import { ethers } from "ethers";
import dotenv from "dotenv";
dotenv.config();

// Set up provider and wallet
const provider = new ethers.JsonRpcProvider("https://base-mainnet.infura.io/v3/85e931233d114d1e9494915d56ec9d54");
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

// Uniswap Router setup
const UNISWAP_ROUTER_ADDRESS = "0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24"; // Uniswap V2 Router on Base
const UNISWAP_ROUTER_ABI = [
  "function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable returns (uint[] memory amounts)",
  "function swapExactTokensForETH(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)",
  "function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts)",
];

export { provider, wallet, UNISWAP_ROUTER_ADDRESS, UNISWAP_ROUTER_ABI };
