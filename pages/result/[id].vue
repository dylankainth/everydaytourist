<template>
    <div class="container mx-auto px-5 pt-3 pb-5">
        <p class="text-3xl">Your results</p>
        <p class="text-lg text-gray-500">We found this for you.</p>

        <div
            class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">

            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ result.title
                }}
            </h5>

            <p>{{ result.summary }}</p>
        </div>
    </div>
</template>

<script>
import { useRoute } from 'vue-router';
export default {
    data() {
        return {
            result: {},
        };
    },
    async mounted() {
        const route = useRoute()
        const id = route.params.id;

        try {
            const response = await fetch(`/pyapi/getPage?id=${id}`);
            this.result = await response.json();
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
};
</script>