/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  async rewrites() {
    return [
      {
        source: "/api/fetchdata",
        destination: process.env.API_FETCH_URL,
      },
    ];
  },
};

module.exports = nextConfig;
