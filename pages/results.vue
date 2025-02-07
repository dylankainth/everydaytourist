<script>
import { useDataStore } from '~/stores/dataStore'

export default {



    computed: {
        jsonData() {
            return this.dataStore.jsonData // Access it just like a regular object
        }
    },
    data() {
        return {
            dataStore: useDataStore(),
            resultState: 'list',
            loaded: false,
            data: null
        }
    },
    async mounted() {

        const response = await fetch('/pyapi/generateRanking', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.jsonData.output)
        })
        this.data = await response.json()
        this.loaded = true
    }


}
</script>
<template>

    <div class="container mx-auto px-5 pt-3 pb-5">

        <div v-if="!loaded">

            <div role="status">
                <svg aria-hidden="true"
                    class="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600 mx-auto"
                    viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                        fill="currentColor" />
                    <path
                        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                        fill="currentFill" />
                </svg>
                <span class="sr-only">Loading...</span>
            </div>

        </div>

        <div v-if="loaded">

            <p class="text-3xl">Your results</p>
            <p class="text-lg text-gray-500">We found this for you.</p>

            <div class="flex justify-center pt-2">
                <div class="inline-flex rounded-lg shadow-sm" role="group">
                    <button type="button" @click="resultState = 'list'"
                        :class="['px-4 py-2 text-sm font-medium text-gray-900 border border-gray-200 rounded-l-lg flex items-center', resultState === 'list' ? 'bg-columbia-500 text-white' : 'bg-white']">
                        <svg :class="['w-6 h-6 mr-2', resultState === 'list' ? 'text-white' : 'text-gray-800']"
                            aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-width="2"
                                d="M9 8h10M9 12h10M9 16h10M4.99 8H5m-.02 4h.01m0 4H5" />
                        </svg>
                        List View
                    </button>

                    <button type="button" @click="resultState = 'map'"
                        :class="['px-4 py-2 text-sm font-medium text-gray-900 border border-gray-200 rounded-r-lg flex items-center', resultState === 'map' ? 'bg-columbia-500 text-white' : 'bg-white']">
                        <svg :class="['w-6 h-6 mr-2', resultState === 'map' ? 'text-white' : 'text-gray-800']"
                            aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                            viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 13a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" />
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17.8 13.938h-.011a7 7 0 1 0-11.464.144h-.016l.14.171c.1.127.2.251.3.371L12 21l5.13-6.248c.194-.209.374-.429.54-.659l.13-.155Z" />
                        </svg>
                        Map View
                    </button>
                </div>
            </div>

            {{ data }}

        </div>

    </div>
</template>