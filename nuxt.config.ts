// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  app: {
    head: {
      link: [
        { rel: 'icon', type: 'image/svg', href: '/logo.svg' }
      ]
    }
  },
  devServer: {
    port: 8020
  },
  routeRules: {
    '/pyapi/**': {
      proxy: process.env.NODE_ENV === "development" ? "http://127.0.0.1:8000/pyapi/**" : "/pyapi/**",
    },
    '/docs': {
      proxy: "http://127.0.0.1:8000/docs",
    },
    '/openapi.json': {
      proxy: "http://127.0.0.1:8000/openapi.json",
    }
  },
  nitro: {
    vercel: {
      config: {
        routes: [{
          "src": "/api/(.*)",
          "dest": "api/index.py"
        }]
      }
    },
  },
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@vite-pwa/nuxt',
    '@vueuse/nuxt',
    '@sidebase/nuxt-auth',
    '@nuxtjs/google-fonts',
    '@pinia/nuxt'
  ],
  googleFonts: {
    families: {
      Poppins: true
    }
  },
  auth: {

    baseURL: process.env.AUTH_ORIGIN,
    originEnvKey: 'AUTH_ORIGIN',
    globalAppMiddleware: true,
    // disableServerSideAuth: true,
    provider: {
      type: 'authjs',
      trustHost: false,
      defaultProvider: 'google',
      addDefaultCallbackUrl: true,
    },

  },
  pwa: {
    manifest: {
      name: 'EveryDayTourist',
      short_name: 'EveryDayYourist',
      start_url: '/',
      display: 'standalone',
      background_color: '#ffffff',
      theme_color: '#ffffff',
      description: 'Discover new places and experiences every day',
      lang: 'en',
      icons: [
        {
          src: '/logo.svg',
          sizes: '192x192',
          type: 'image/svg',
        },
        {
          src: '/logo512.png',
          sizes: '512x512',
          type: 'image/png',
        },
      ]
    },
  },
})