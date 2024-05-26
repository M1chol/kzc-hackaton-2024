<script setup>
import { favs } from '../main.js'
</script>
<template>
    <!-- <div v-for="item in favs" class="favourite" :key="item.ID">
        {{ item }}
    </div> -->
    <div class="favourite">test1</div>
    <div class="favourite">test2</div>
    <div class="favourite">test3</div>

</template>


<style scoped>
    .favourite {
        box-shadow: 0px 10px 20px -18px;
        background-color: #EEEEEE;
        width: 100px;
        height: 50px;
        border-radius: 20px;
        text-align: center;
        line-height: 50px;
        font-weight: bold;
    }
</style>