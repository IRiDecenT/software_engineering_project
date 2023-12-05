<script setup>
    import { onBeforeUpdate } from 'vue';
    import Album from '@/components/Album.vue';
    import { useRoute } from 'vue-router';
    const route = useRoute();
    let albumId = route.params.albumId;
    onBeforeUpdate(()=>{
        albumId = route.params.albumId;
        console.log(albumId);
    })

</script>

<template>
    <main class="about">
        <div>{{ albumId }}</div>
        <Album :albumId="albumId"/>
    </main>
</template>

<style>
@media (min-width: 1024px) {
.about {
    min-height: 100vh;
    display: flex;
    align-items: center;
    background-color: #1a1a1a;
}
}
</style>