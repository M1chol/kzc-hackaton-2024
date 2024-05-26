<template>
    <div id="menu">
        <div id="profile">
            <img src="../assets/pp_placeholder.jpg" id="pp" @click="() => logIn()">
        </div>
        <div id="schedule" class="option">Plan Lekcji</div>
        <div id="calculator" class="option">Kalkulator Sredniej</div>
        <div id="miniwiki" class="option">Poradnik</div>
    </div>
</template>

<script setup>
const emit = defineEmits(['logIn']);
const logIn = () => {
  emit('logIn');
}
</script>

<style>
#pp {
    height: 150px;
    width: 150px;
    border-radius: 75px;
}
#profile {
    height: 150px;
    width: 150px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 70px;
}
#menu {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap:20px;
    padding: 20px;
    overflow-y: scroll;
    overflow-x: hidden;
    touch-action: pan-y;
}
.option {
    text-transform: uppercase;
    padding: 0;
    text-align: center;
    line-height: 70px;
    margin-left: auto;
    margin-right: auto;
    width: 320px;
    height: 70px;
    background-color: #EEEEEE;
    border-radius: 20px;
}
</style>