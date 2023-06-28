/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  async rewrites() {
    return [
      {
        source: "/api/fetchdata",
        destination:
          "https://f5fqv3gg77.execute-api.us-east-1.amazonaws.com/Prod/fetch",
      },
    ];
  },
};

module.exports = nextConfig;
