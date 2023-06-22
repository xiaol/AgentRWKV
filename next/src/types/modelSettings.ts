import { type Language } from "../utils/languages";

export const [GPT_35_TURBO, GPT_35_TURBO_16K, GPT_4] = [
  "RWKV-world-7B" as const,
  "gpt-3.5-turbo-16k" as const,
  "gpt-4" as const,
];
export const GPT_MODEL_NAMES = [GPT_35_TURBO, GPT_35_TURBO_16K, GPT_4];
export type GPTModelNames = "RWKV-world-7B" | "gpt-3.5-turbo-16k" | "gpt-4";

export const MAX_TOKENS: Record<GPTModelNames, number> = {
  "RWKV-world-7B": 4000,
  "gpt-3.5-turbo-16k": 16000,
  "gpt-4": 4000,
};

export interface ModelSettings {
  language: Language;
  customApiKey: string;
  customModelName: GPTModelNames;
  customTemperature: number;
  customMaxLoops: number;
  maxTokens: number;
}
