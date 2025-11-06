/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbo: false, // Desativa o Turbopack (causador do erro)
  },
};

export default nextConfig;
