// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    port: 8020
  },
  ssr: false,
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@vite-pwa/nuxt',
    '@vueuse/nuxt',
  ],
  pwa: {
    manifest: {
      name: 'EveryDayTourist',
      short_name: 'EveryDayYourist',
      start_url: '/',
      display: 'standalone',
      background_color: '#ffffff',
      theme_color: '#ffffff',
      icons: [
        {
          src: '/image.png',
          sizes: '192x192',
          type: 'image/png',
        },
      ]
    },
  },
})