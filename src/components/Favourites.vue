<script setup>
import { favs } from '../main.js'
</script>
<template>
    <div v-for="item in favs" class="favourite" :key="item.POSTID">
        {{ item.PostName }}
    </div>
</template>


<style scoped>
    .favourite {
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        box-shadow: 0px 10px 20px -18px;
        background-color: #EEEEEE;
        padding-left: 15px;
        padding-right: 15px;
        width: 25%;
        height: 50px;
        border-radius: 20px;
        text-align: center;
        line-height: 50px;
    }
</style>