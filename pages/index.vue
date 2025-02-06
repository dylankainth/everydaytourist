<template>
  <div>

    <div class="container mx-auto px-5 pt-3 pb-5">


      <p class="text-3xl">Welcome</p>
      <p class="text-lg text-gray-500">Let's find you some deals.</p>



      <div ref="el">
        <div class="pt-5" v-for="discount in data" :key="discount.offerUid">
          <NuxtLink :href="`/discounts/${discount.offerUid}`"
            class="flex bg-white border border-gray-200 rounded-lg shadow max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700 h-36">
            <img class="object-cover w-1/3 rounded-s-lg h-full" :src="discount.defaultImage" alt="">
            <div class="flex flex-col justify-between p-4 leading-normal w-2/3">
              <h5 class="mb-2 text-sm font-bold tracking-tight text-gray-900 dark:text-white">
                {{ discount.title }}
              </h5>
              <img class="w-20 h-5" :src="discount.brandLogo" alt="">
              <p class="mb-3 font-normal text-xs text-gray-700 dark:text-gray-400">
                {{ discount.brandName }}
              </p>
            </div>
          </NuxtLink>
        </div>
      </div>

      <button @click="resetList()">
        Reset
      </button>



    </div>






  </div>

</template>

<script setup lang="ts">

const discountData = await $fetch('/api/getDiscounts?page=1')
var discounts = discountData.hits

import { useInfiniteScroll } from '@vueuse/core'
import { ref } from 'vue'

const el = ref<HTMLElement | null>(null)
const data = ref(discounts)
const pages = ref(1)
const totalPages = ref(discountData.nbPages);

const { reset } = useInfiniteScroll(
  el,
  async () => {
    // load more
    pages.value++
    const newDiscountData = await $fetch(`/api/getDiscounts?page=${pages.value}`)
    const newDiscounts = newDiscountData.hits
    data.value = [...data.value, ...newDiscounts]
  },
  {
    distance: 1,
    canLoadMore: () => {
      console.log(pages.value, totalPages.value)
      if (pages.value >= totalPages.value) {
        return false
      }
      return true // for demo purposes
    },
  }
)

function resetList() {
  data.value = []
  reset()
}
</script>
