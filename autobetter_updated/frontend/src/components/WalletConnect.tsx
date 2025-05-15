import React from 'react';
import WalletConnectProvider from '@walletconnect/web3-provider';
import Web3 from 'web3';

export default function WalletConnect({ onConnect }: { onConnect: (addr: string) => void }) {
  const connect = async () => {
    const provider = new WalletConnectProvider({ infuraId: process.env.REACT_APP_INFURA_ID });
    await provider.enable();
    const web3 = new Web3(provider as any);
    const accounts = await web3.eth.getAccounts();
    onConnect(accounts[0]);
  };
  return <button onClick={connect}>Connect Wallet</button>;
}
