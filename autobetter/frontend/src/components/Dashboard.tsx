import React, { useEffect, useState } from 'react';
import WalletConnect from './WalletConnect';
import MarketList from './MarketList';
import { fetchMarkets, Market } from '../services/api';

export default function Dashboard() {
  const [address, setAddress] = useState<string>();
  const [markets, setMarkets] = useState<Market[]>([]);

  useEffect(() => { fetchMarkets().then(setMarkets); }, []);
  return (
    <div>
      {!address
        ? <WalletConnect onConnect={setAddress} />
        : <p>Connected: {address}</p>}
      <MarketList markets={markets} />
    </div>
  );
}
