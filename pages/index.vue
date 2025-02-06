<script setup>

const { data } = useAuth()
</script>


<template>
  <div>

    <div class="container mx-auto px-5 pt-3 pb-5">


      <p class="text-3xl">Welcome</p>
      Hello {{ data }}!
      <p class="text-lg text-gray-500">Let's find you some deals.</p>


    </div>

  </div>

</template>
