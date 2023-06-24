import Head from "next/head";

const AppHead = () => {
  // Do not translate. Head attributes won't have access to i18n.
  const description = "Assemble, configure, and deploy autonomous AI Agents in your browser.";

  return (
    <Head>
      <title>AgentRWKV</title>
      <meta name="description" content={description} />
      <meta name="twitter:site" content="@AgentRWKV" />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content="AgentRWKV 🤖" />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content="https://agentrwkv.ai-creator.net/banner.png" />
      <meta name="twitter:image:width" content="1280" />
      <meta name="twitter:image:height" content="640" />
      <meta property="og:title" content="AgentRWKV: Autonomous AI in your browser 🤖" />
      <meta property="og:description" content={description} />
      <meta property="og:url" content="https://agentrwkv.ai-creator.net/" />
      <meta property="og:image" content="https://agentrwkv.ai-creator.net/banner.png" />
      <meta property="og:image:width" content="1280" />
      <meta property="og:image:height" content="640" />
      <meta property="og:type" content="website" />
      <meta
        name="google-site-verification"
        content="sG4QDkC8g2oxKSopgJdIe2hQ_SaJDaEaBjwCXZNkNWA"
      />
      <link rel="icon" href="/favicon.ico" />
    </Head>
  )
}

export default AppHead;