import { defineStore } from 'pinia'

export const useDataStore = defineStore('dataStore', {
    state: () => ({
        jsonData: {} as Record<string, any>
    }),
    actions: {
        // Overwrites the existing JSON object
        updateData(newData: Record<string, any>) {
            this.jsonData = newData
        },
        clearData() {
            this.jsonData = {}
        }
    }
})
