<script setup lang="ts">
definePageMeta({
    auth: { unauthenticatedOnly: true, navigateAuthenticatedTo: '/' }
})

const { signIn, status, data } = useAuth()
</script>

<template>
    <div>
        <p>Sign-In Options:</p>
        <button @click="signIn('google')">
            Google
        </button>

        {{ status }}

        {{ data }}

    </div>
</template>