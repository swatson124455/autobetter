import React from 'react';
import { Market } from '../services/api';

export default function MarketList({ markets }: { markets: Market[] }) {
  return (
    <div>
      {markets.map(m => (
        <div key={m.id}>
          <h3>{m.name}</h3>
          <p>Yes: {m.probabilities.yes.toFixed(2)}</p>
        </div>
      ))}
    </div>
  );
}
