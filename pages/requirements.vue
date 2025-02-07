<template>
    <div>

        <div class="container mx-auto px-5 pt-3 pb-5">

            <p class="text-3xl">Welcome</p>
            <p class="text-lg text-gray-500">Let's find you something to do.</p>


            <div class="pt-6 flex justify-center">
                <div class="flex items-center bg-gray-100 p-4 rounded-2xl shadow-md w-80">
                    <div class="px-2 w-full">
                        <p class="font-bold text-lg text-gray-900">Your Location</p>

                        <div v-if="location.status === 'waiting'">
                            <div class="pt-2 flex justify-center items-center">
                                <button @click="getLocation()" type="button"
                                    class="text-white bg-columbia-600 hover:bg-columbia-700 focus:ring-4 focus:ring-columbia-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-columbia-600 dark:hover:bg-columbia-700 focus:outline-none dark:focus:ring-columbia-800">
                                    Get my location</button>
                            </div>
                        </div>



                        <div v-if="location.status === 'loading'">

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



                        <div v-if="location.status === 'success'">
                            <div class="pt-2">
                                <p class="text-gray-500">Latitude: {{ location.data.coords.latitude }}</p>
                                <p class="text-gray-500">Longitude: {{ location.data.coords.longitude }}</p>
                            </div>
                        </div>

                        <div v-if="location.status === 'error'">
                            <div class="pt-2">
                                <p class="text-red-500">Error getting location</p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>


            <div class="pt-6 flex justify-center" v-if="location.data">
                <div class="flex items-center bg-gray-100 p-4 rounded-2xl shadow-md w-80">
                    <div class="px-2 w-full">

                        <div v-if="willItRain">
                            <p class="font-bold text-lg text-gray-900">Got a brolly?</p>
                            <p class="text-gray-600 text-sm">It might rain over the next few hours</p>
                        </div>

                        <div v-if="!willItRain">
                            <p class="font-bold text-lg text-gray-900">Sunny side up!</p>
                            <p class="text-gray-600 text-sm">The weather looks good!</p>
                        </div>

                        <div class="inline-flex rounded-lg shadow-sm pt-2" role="group">
                            <button type="button" @click="weather.outdoorActivities = true"
                                :class="['px-4 py-2 text-sm font-medium text-gray-900 border border-gray-200 rounded-l-lg flex items-center', weather.outdoorActivities ? 'bg-columbia-500 text-white' : 'bg-white']">
                                <svg :class="['w-6 h-6 mr-2', weather.outdoorActivities ? 'text-white' : 'text-gray-800']"
                                    aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                                    fill="none" viewBox="0 0 24 24">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M12 5V3m0 18v-2M7.05 7.05 5.636 5.636m12.728 12.728L16.95 16.95M5 12H3m18 0h-2M7.05 16.95l-1.414 1.414M18.364 5.636 16.95 7.05M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z" />

                                </svg>
                                Outdoor Activities
                            </button>


                            <button type="button" @click="weather.outdoorActivities = false"
                                :class="['px-4 py-2 text-sm font-medium text-gray-900 border border-gray-200 rounded-r-lg flex items-center', !weather.outdoorActivities ? 'bg-columbia-500 text-white' : 'bg-white']">

                                <svg :class="['w-6 h-6 mr-2', !weather.outdoorActivities ? 'text-white' : 'text-gray-800']"
                                    width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
                                    fill="none" stroke-linecap="round" stroke-linejoin="round">
                                    <path stroke="none" d="M0 0h24v24H0z" />
                                    <path d="M7 18a4.6 4.4 0 0 1 0 -9h0a5 4.5 0 0 1 11 2h1a3.5 3.5 0 0 1 0 7" />
                                    <path d="M11 13v2m0 3v2m4 -5v2m0 3v2" />
                                </svg>
                                Indoor Activities
                            </button>
                        </div>

                    </div>
                </div>
            </div>


            <div class="pt-6 flex justify-center" v-if="location.data && weather.outdoorActivities != null">
                <div class="flex items-center bg-gray-100 p-4 rounded-2xl shadow-md w-80">
                    <div class="px-2 w-full">
                        <p class="font-bold text-lg text-gray-900">Get those steps in?</p>
                        <p class="text-gray-600 text-sm">Walking Distance: {{ walkingDistance }}m</p>


                        <input id="default-range" type="range" v-model="walkingDistance" min="100" max="3000" step="100"
                            class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700">

                    </div>
                </div>
            </div>

            <div class="pt-6 flex justify-center" v-if="location.data && weather.outdoorActivities != null">
                <div class="flex items-center p-4 ">
                    <div class="px-2 w-full">
                        <button type="button"
                            class="text-white bg-columbia-600 hover:bg-columbia-700 focus:ring-4 focus:ring-columbia-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-columbia-600 dark:hover:bg-columbia-700 focus:outline-none dark:focus:ring-columbia-800">
                            Submit</button>
                    </div>
                </div>
            </div>





        </div>

    </div>

</template>


<script>
export default {
    data() {
        return {
            location: {
                status: 'waiting',
                data: null,
            },
            weather: {
                temperature: null,
                precipitation: null,
                outdoorActivities: null
            },
            walkingDistance: 100
        }
    },

    methods: {
        async getLocation() {

            this.location.status = 'loading';
            try {
                const pos = await new Promise((resolve, reject) => {
                    navigator.geolocation.getCurrentPosition(resolve, reject);
                });
                this.location.data = pos;
                this.location.status = 'success';
            } catch (err) {
                this.location.status = 'error';
                console.error(err);
            }
        }
    },

    watch: {
        location: {
            async handler(val) {
                if (val.data) {

                    const weatherData = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=` + val.data.coords.latitude + `&longitude=` + val.data.coords.longitude + `&hourly=temperature_2m,precipitation_probability&forecast_days=1`)

                    const weatherDataDecoded = await weatherData.json()

                    this.weather.temperature = weatherDataDecoded.hourly.temperature_2m;
                    this.weather.precipitation = weatherDataDecoded.hourly.precipitation_probability;
                }
            },
            deep: true
        }

    },

    computed: {
        willItRain() {
            // get the current hour
            const currentHour = new Date().getHours();

            if (!this.weather.precipitation) {
                return false;
            }
            // get the precipitation probability for the current hour and next 3 hours
            const precipitationProbabilities = this.weather.precipitation.slice(currentHour, currentHour + 3);

            for (const probability of precipitationProbabilities) {
                if (probability > 50) {

                    if (this.weather.outdoorActivities == null) {
                        this.weather.outdoorActivities = false;
                    }
                    return true;
                }
            }
            if (this.weather.outdoorActivities == null) {
                this.weather.outdoorActivities = true;
            }

            return false;
        }
    }


}
</script>