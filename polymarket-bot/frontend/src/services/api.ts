export interface Market {
  id: string;
  name: string;
  probabilities: { yes: number; no: number };
}

export async function fetchMarkets(): Promise<Market[]> {
  const res = await fetch('/markets');
  return res.json();
}
