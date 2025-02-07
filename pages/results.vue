<script>
import { useDataStore } from '~/stores/dataStore'

export default {

    methods: {
        walkingTimeMins(seconds) {
            return Math.round(seconds / 60)
        }
    },

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

            <div class="pt-5" v-if="resultState === 'list'">

                <div v-for="card in data.body" class="pt-2">
                    <a href="#"
                        class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">

                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ card.title
                            }}
                        </h5>

                        <p class="font-normal text-gray-700 dark:text-gray-400 flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                                fill="#5f6368">
                                <path
                                    d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z" />
                            </svg>
                            &nbsp; {{ card.views }} Wikipedia Views
                        </p>

                        <p class="font-normal text-gray-700 dark:text-gray-400 flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                                fill="#5f6368" class="mr-2">
                                <path
                                    d="m280-40 112-564-72 28v136h-80v-188l202-86q14-6 29.5-7t29.5 4q14 5 26.5 14t20.5 23l40 64q26 42 70.5 69T760-520v80q-70 0-125-29t-94-74l-25 123 84 80v300h-80v-260l-84-64-72 324h-84Zm260-700q-33 0-56.5-23.5T460-820q0-33 23.5-56.5T540-900q33 0 56.5 23.5T620-820q0 33-23.5 56.5T540-740Z" />
                            </svg>
                            {{ walkingTimeMins(card.walkingTime) }} minutes
                        </p>

                    </a>

                </div>


            </div>

            <div class="pt-5" v-if="resultState === 'map'">


                <LMap style="width:90vw;height:60vh" :zoom="15"
                    :center="[jsonData.output.location.coords.latitude, jsonData.output.location.coords.longitude]"
                    :use-global-leaflet="false">
                    <LTileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors"
                        layer-type="base" name="OpenStreetMap" />

                    <LMarker
                        :lat-lng="[jsonData.output.location.coords.latitude, jsonData.output.location.coords.longitude]">
                    </LMarker>

                    <div v-for="pin in data.body">

                        <LMarker :lat-lng="[pin.lat, pin.lon]">
                            <LPopup>
                                <p>{{ pin.title }}</p>
                            </LPopup>
                        </LMarker>
                    </div>
                </LMap>

            </div>

        </div>
    </div>
</template>