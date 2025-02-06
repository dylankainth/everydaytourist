<template>
    <div>
        <div class="container mx-auto px-5 pt-3 pb-5">

            <img :src="discountData.defaultImage" />
            <p class="text-3xl">{{ discountData.title }}</p>
            <p class="text-lg text-gray-500">{{ discountData.tac }}</p>
            <p class="text-lg text-gray-500">{{ discountData.description }}</p>

        </div>

    </div>
</template>
<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
const discountFetched = await $fetch('/api/getDiscount?offerUid=' + route.params.id)

var discountData = ref(discountFetched);


</script>
