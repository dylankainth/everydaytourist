<script setup>

const { data } = useAuth()
</script>


<template>
  <div class="flex items-center justify-center min-h-screen">

    <div class="container mx-auto px-5 pt-3 pb-5">
      <div class="hero text-center my-10">
        <h1 class="text-5xl font-bold">Everyday Tourist</h1>
        <p class="text-xl mt-4">Discover new places and experiences every day</p>

        <div class="mt-10">
          <NuxtLink to="/requirements" type="button"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
            Get Started</NuxtLink>

        </div>
      </div>

    </div>

  </div>

</template>
