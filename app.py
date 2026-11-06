from flask import Flask, jsonify, render_template_string
from datetime import datetime
import random

app = Flask(__name__)

# ============================================================
# MINECRAFT UNIVERSE - Complete Game Information Hub
# Single-file Flask application with all Minecraft modes & features
# ============================================================

HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#3d9c3d">
<meta name="description" content="Minecraft Universe - Explore all game modes, features, mobs, biomes, and blocks in one beautiful space.">
<title>Minecraft Universe - Complete Game Guide</title>

<style>
:root{
 --bg:#1a1a1a;--surface:#2d2d2d;--ink:#e8e8e8;--muted:#a0a0a0;
 --grass:#3d9c3d;--dirt:#8b6f47;--stone:#7f7f7f;--diamond:#5cb3ff;
 --redstone:#ff3333;--gold:#ffaa00;--emerald:#00ff00;--nether:#8b0000;
 --shadow:0 10px 40px rgba(0,0,0,.5);
 --radius:12px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
    font-family:'Minecraft',Monaco,'Courier New',monospace;
    background:var(--bg);
    color:var(--ink);
    overflow-x:hidden;
    line-height:1.6;
}
button,input,textarea,select{font:inherit}
button{cursor:pointer}
a{text-decoration:none;color:inherit}
.container{width:min(1200px,92%);margin:auto}

/* Header */
.topbar{
    height:80px;
    position:sticky;
    top:0;
    z-index:900;
    background:rgba(29,29,29,.95);
    backdrop-filter:blur(20px);
    border-bottom:4px solid var(--grass);
    display:flex;
    align-items:center;
}
.nav{display:flex;align-items:center;justify-content:space-between;gap:20px}
.brand{
    font-weight:bold;
    font-size:28px;
    letter-spacing:2px;
    color:var(--grass);
    text-shadow:2px 2px 0 #000;
}
.navlinks{display:flex;gap:25px;font-size:14px;font-weight:bold}
.navlinks a{
    color:var(--muted);
    padding:8px 15px;
    border:2px solid transparent;
    transition:.3s;
}
.navlinks a:hover{
    color:var(--grass);
    border:2px solid var(--grass);
    background:rgba(61,156,61,.1);
}

/* Hero Section */
.hero{
    min-height:calc(100vh - 80px);
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:80px 0;
    background:linear-gradient(180deg,#1a1a1a 0%,#0d4d0d 100%);
    position:relative;
    overflow:hidden;
}
.hero:before{
    content:"⛏️";
    position:absolute;
    font-size:400px;
    opacity:.05;
    animation:float 6s ease-in-out infinite;
}
.hero h1{
    font-size:clamp(48px,8vw,90px);
    letter-spacing:4px;
    margin:20px 0;
    color:var(--grass);
    text-shadow:4px 4px 0 #000;
}
.hero p{
    font-size:20px;
    color:var(--muted);
    max-width:700px;
    margin:20px auto;
}
.hero-buttons{
    display:flex;
    gap:15px;
    justify-content:center;
    flex-wrap:wrap;
    margin-top:30px;
}

/* Buttons */
.btn{
    border:0;
    border-radius:var(--radius);
    padding:15px 30px;
    font-weight:bold;
    transition:.2s;
    text-transform:uppercase;
    letter-spacing:1px;
    box-shadow:var(--shadow);
}
.btn:hover{transform:translateY(-3px)}
.btn-primary{
    background:var(--grass);
    color:#fff;
    border:3px solid #2d7a2d;
}
.btn-secondary{
    background:var(--stone);
    color:#fff;
    border:3px solid #5f5f5f;
}
.btn-nether{
    background:var(--nether);
    color:#fff;
    border:3px solid #660000;
}
.btn-diamond{
    background:var(--diamond);
    color:#fff;
    border:3px solid #3a8fd9;
}

/* Section */
.section{padding:80px 0}
.section-alt{background:var(--surface)}
.section-head{text-align:center;margin-bottom:50px}
.section-head h2{
    font-size:clamp(36px,5vw,60px);
    color:var(--grass);
    text-shadow:3px 3px 0 #000;
    margin-bottom:15px;
}
.section-head p{color:var(--muted);font-size:18px}

/* Grid Layouts */
.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:25px;
}
.grid-2{grid-template-columns:repeat(auto-fit,minmax(400px,1fr))}
.grid-4{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}

/* Cards */
.card{
    background:var(--surface);
    border:3px solid #444;
    border-radius:var(--radius);
    padding:30px;
    transition:.3s;
    position:relative;
    overflow:hidden;
}
.card:hover{
    transform:translateY(-5px);
    border-color:var(--grass);
    box-shadow:0 15px 50px rgba(61,156,61,.3);
}
.card-icon{
    font-size:60px;
    margin-bottom:15px;
    display:block;
}
.card h3{
    font-size:24px;
    margin-bottom:10px;
    color:var(--grass);
}
.card p{
    color:var(--muted);
    line-height:1.7;
}
.card .badge{
    display:inline-block;
    padding:5px 12px;
    background:var(--grass);
    color:#fff;
    border-radius:20px;
    font-size:11px;
    margin-top:10px;
    font-weight:bold;
}

/* Special Cards */
.mode-card{border-left:6px solid var(--grass)}
.mode-card.survival{border-left-color:var(--grass)}
.mode-card.creative{border-left-color:var(--gold)}
.mode-card.adventure{border-left-color:var(--diamond)}
.mode-card.spectator{border-left-color:var(--muted)}
.mode-card.hardcore{border-left-color:var(--redstone)}

/* Tabs */
.tabs{
    display:flex;
    gap:10px;
    margin-bottom:30px;
    flex-wrap:wrap;
    justify-content:center;
}
.tab-btn{
    padding:12px 25px;
    background:var(--surface);
    border:2px solid #444;
    border-radius:var(--radius);
    color:var(--muted);
    font-weight:bold;
    transition:.3s;
}
.tab-btn.active{
    background:var(--grass);
    color:#fff;
    border-color:var(--grass);
}
.tab-btn:hover{border-color:var(--grass)}

.tab-content{display:none}
.tab-content.active{display:block}

/* Stats */
.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
    gap:20px;
    margin:40px 0;
}
.stat{
    background:var(--surface);
    border:3px solid #444;
    border-radius:var(--radius);
    padding:25px;
    text-align:center;
}
.stat-value{
    font-size:42px;
    font-weight:bold;
    color:var(--grass);
    display:block;
}
.stat-label{
    color:var(--muted);
    font-size:14px;
}

/* List */
.feature-list{
    list-style:none;
    padding:0;
}
.feature-list li{
    padding:12px 0;
    border-bottom:1px solid #444;
    color:var(--muted);
}
.feature-list li:before{
    content:"⛏️ ";
    color:var(--grass);
    font-weight:bold;
}

/* Footer */
footer{
    padding:50px 0;
    background:#0d0d0d;
    border-top:4px solid var(--grass);
    text-align:center;
}
footer p{color:var(--muted);margin:10px 0}

/* Animations */
@keyframes float{
    0%,100%{transform:translateY(0)}
    50%{transform:translateY(-30px)}
}
@keyframes spin{
    to{transform:rotate(360deg)}
}

/* Responsive */
@media(max-width:768px){
    .hero h1{font-size:42px}
    .grid-2,.grid-4{grid-template-columns:1fr}
    .navlinks{display:none}
}

/* Minecraft Pixel Font Fallback */
body{
    image-rendering:pixelated;
    -ms-interpolation-mode:nearest-neighbor;
}
</style>
</head>

<body>

<header class="topbar">
<div class="container nav">
<div class="brand">⛏️ MINECRAFT UNIVERSE</div>
<nav class="navlinks">
<a href="#modes">Game Modes</a>
<a href="#features">Features</a>
<a href="#mobs">Mobs</a>
<a href="#biomes">Biomes</a>
<a href="#blocks">Blocks</a>
</nav>
</div>
</header>

<main>

<!-- HERO -->
<section class="hero">
<div class="container">
<h1>🎮 MINECRAFT UNIVERSE</h1>
<p>
Explore the complete world of Minecraft - all game modes, features, mobs, biomes, 
and blocks in one comprehensive guide. Build, survive, explore, and create!
</p>
<div class="hero-buttons">
<button class="btn btn-primary" onclick="scrollTo('#modes')">Explore Game Modes</button>
<button class="btn btn-diamond" onclick="scrollTo('#features')">View Features</button>
<button class="btn btn-nether" onclick="randomFact()">Random Fact</button>
</div>
</div>
</section>

<!-- GAME MODES -->
<section id="modes" class="section">
<div class="container">
<div class="section-head">
<h2>🎮 GAME MODES</h2>
<p>Choose your playstyle - from peaceful building to intense survival challenges</p>
</div>

<div class="grid">
<div class="card mode-card survival">
<span class="card-icon">⚔️</span>
<h3>Survival Mode</h3>
<p>
Gather resources, craft tools, build shelters, and survive against hostile mobs. 
Manage health and hunger while exploring the world. The classic Minecraft experience!
</p>
<span class="badge">MOST POPULAR</span>
</div>

<div class="card mode-card creative">
<span class="card-icon">🎨</span>
<h3>Creative Mode</h3>
<p>
Unlimited resources, fly around the world, and build without restrictions. 
Perfect for architects and builders who want to focus on creativity without survival challenges.
</p>
<span class="badge">NO LIMITS</span>
</div>

<div class="card mode-card adventure">
<span class="card-icon">🗺️</span>
<h3>Adventure Mode</h3>
<p>
Designed for custom maps and adventures. Players can only break blocks with proper tools, 
making it perfect for map makers who want controlled gameplay experiences.
</p>
<span class="badge">MAP MAKERS</span>
</div>

<div class="card mode-card spectator">
<span class="card-icon">👻</span>
<h3>Spectator Mode</h3>
<p>
Fly through blocks, observe the world without interaction, and view from mob perspectives. 
Perfect for exploring builds or watching multiplayer action without interference.
</p>
<span class="badge">OBSERVER</span>
</div>

<div class="card mode-card hardcore">
<span class="card-icon">💀</span>
<h3>Hardcore Mode</h3>
<p>
Survival mode with permanent death and locked difficulty. One life, maximum challenge! 
When you die, the world is over. Only for the bravest players.
</p>
<span class="badge">EXTREME</span>
</div>
</div>
</div>
</section>

<!-- FEATURES -->
<section id="features" class="section section-alt">
<div class="container">
<div class="section-head">
<h2>✨ CORE FEATURES</h2>
<p>Everything that makes Minecraft the ultimate sandbox adventure</p>
</div>

<div class="tabs">
<button class="tab-btn active" onclick="switchTab('building')">Building</button>
<button class="tab-btn" onclick="switchTab('crafting')">Crafting</button>
<button class="tab-btn" onclick="switchTab('exploration')">Exploration</button>
<button class="tab-btn" onclick="switchTab('combat')">Combat</button>
<button class="tab-btn" onclick="switchTab('redstone')">Redstone</button>
<button class="tab-btn" onclick="switchTab('farming')">Farming</button>
</div>

<div id="building" class="tab-content active">
<div class="grid-2">
<div class="card">
<span class="card-icon">🏗️</span>
<h3>Creative Building</h3>
<ul class="feature-list">
<li>Place and break blocks to build anything imaginable</li>
<li>Thousands of block types with unique properties</li>
<li>Build houses, castles, cities, or pixel art</li>
<li>Structure blocks for advanced builders</li>
<li>Scaffolding for easy vertical building</li>
</ul>
</div>
<div class="card">
<span class="card-icon">🎨</span>
<h3>Design Elements</h3>
<ul class="feature-list">
<li>Decorative blocks: stairs, slabs, fences, walls</li>
<li>Colored concrete, terracotta, and wool</li>
<li>Glass panes and stained glass</li>
<li>Lighting options: torches, lanterns, glowstone</li>
<li>Custom banners and armor stands</li>
</ul>
</div>
</div>
</div>

<div id="crafting" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">⚒️</span>
<h3>Crafting System</h3>
<ul class="feature-list">
<li>3x3 crafting grid for creating items</li>
<li>Hundreds of crafting recipes to discover</li>
<li>Craft tools, weapons, armor, and blocks</li>
<li>Shapeless and shaped recipes</li>
<li>Recipe book for easy reference</li>
</ul>
</div>
<div class="card">
<span class="card-icon">🔨</span>
<h3>Advanced Crafting</h3>
<ul class="feature-list">
<li>Smithing table for upgrading gear</li>
<li>Enchanting table for magical enhancements</li>
<li>Brewing stand for potions</li>
<li>Anvil for repairing and combining</li>
<li>Stonecutter for efficient block crafting</li>
</ul>
</div>
</div>
</div>

<div id="exploration" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">🧭</span>
<h3>World Exploration</h3>
<ul class="feature-list">
<li>Infinite procedurally generated worlds</li>
<li>Multiple dimensions: Overworld, Nether, End</li>
<li>Diverse biomes with unique features</li>
<li>Villages, temples, and dungeons to discover</li>
<li>Ocean monuments and shipwrecks</li>
</ul>
</div>
<div class="card">
<span class="card-icon">🗺️</span>
<h3>Navigation Tools</h3>
<ul class="feature-list">
<li>Maps and compasses for navigation</li>
<li>Lodestone for custom compass points</li>
<li>Coordinates display (F3 on Java)</li>
<li>Boat and minecart transportation</li>
<li>Elytra wings for flying</li>
</ul>
</div>
</div>
</div>

<div id="combat" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">⚔️</span>
<h3>Combat System</h3>
<ul class="feature-list">
<li>Swords, axes, and tridents for melee combat</li>
<li>Bows, crossbows for ranged attacks</li>
<li>Shields for blocking attacks</li>
<li>Critical hits and sweeping attacks</li>
<li>Attack cooldown mechanics (Java Edition)</li>
</ul>
</div>
<div class="card">
<span class="card-icon">🛡️</span>
<h3>Defense & Armor</h3>
<ul class="feature-list">
<li>Leather, iron, diamond, and netherite armor</li>
<li>Armor provides damage reduction</li>
<li>Enchantments for enhanced protection</li>
<li>Shields block arrows and attacks</li>
<li>Potions for combat advantages</li>
</ul>
</div>
</div>
</div>

<div id="redstone" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">🔴</span>
<h3>Redstone Basics</h3>
<ul class="feature-list">
<li>Redstone dust transmits power signals</li>
<li>Redstone torches, repeaters, and comparators</li>
<li>Buttons, levers, and pressure plates</li>
<li>Pistons and sticky pistons for moving blocks</li>
<li>Observers detect block changes</li>
</ul>
</div>
<div class="card">
<span class="card-icon">⚡</span>
<h3>Advanced Circuits</h3>
<ul class="feature-list">
<li>Build automatic farms and doors</li>
<li>Create complex logic gates</li>
<li>Command blocks for custom mechanics</li>
<li>Hopper systems for item sorting</li>
<li>Flying machines and elevators</li>
</ul>
</div>
</div>
</div>

<div id="farming" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">🌾</span>
<h3>Agriculture</h3>
<ul class="feature-list">
<li>Grow wheat, carrots, potatoes, and beetroot</li>
<li>Plant trees and harvest wood</li>
<li>Breed animals for resources</li>
<li>Automatic farms with redstone</li>
<li>Bone meal for instant growth</li>
</ul>
</div>
<div class="card">
<span class="card-icon">🐄</span>
<h3>Animal Husbandry</h3>
<ul class="feature-list">
<li>Breed cows, pigs, chickens, and sheep</li>
<li>Feed animals to produce offspring</li>
<li>Collect milk, eggs, and wool</li>
<li>Tame horses, cats, and wolves</li>
<li>Build automated animal farms</li>
</ul>
</div>
</div>
</div>

</div>
</section>

<!-- MOBS -->
<section id="mobs" class="section">
<div class="container">
<div class="section-head">
<h2>👹 MOBS & CREATURES</h2>
<p>Friendly allies, dangerous enemies, and neutral creatures</p>
</div>

<div class="tabs">
<button class="tab-btn active" onclick="switchTab('hostile')">Hostile</button>
<button class="tab-btn" onclick="switchTab('passive')">Passive</button>
<button class="tab-btn" onclick="switchTab('neutral')">Neutral</button>
<button class="tab-btn" onclick="switchTab('bosses')">Bosses</button>
</div>

<div id="hostile" class="tab-content active">
<div class="grid-4">
<div class="card">
<span class="card-icon">🧟</span>
<h3>Zombie</h3>
<p>Slow but relentless undead mob. Burns in sunlight. Drops rotten flesh.</p>
</div>
<div class="card">
<span class="card-icon">💀</span>
<h3>Skeleton</h3>
<p>Ranged attacker with bow. Burns in sunlight. Drops bones and arrows.</p>
</div>
<div class="card">
<span class="card-icon">🕷️</span>
<h3>Spider</h3>
<p>Can climb walls and fit through small spaces. Neutral in daylight.</p>
</div>
<div class="card">
<span class="card-icon">💥</span>
<h3>Creeper</h3>
<p>Silent stalker that explodes near players. Drops gunpowder. Very dangerous!</p>
</div>
<div class="card">
<span class="card-icon">👁️</span>
<h3>Enderman</h3>
<p>Teleporting mob. Becomes hostile when looked at. Drops ender pearls.</p>
</div>
<div class="card">
<span class="card-icon">🔥</span>
<h3>Blaze</h3>
<p>Nether mob that shoots fireballs. Drops blaze rods for brewing.</p>
</div>
<div class="card">
<span class="card-icon">👻</span>
<h3>Phantom</h3>
<p>Flying undead that attacks players who haven't slept. Drops phantom membrane.</p>
</div>
<div class="card">
<span class="card-icon">🏹</span>
<h3>Pillager</h3>
<p>Hostile illager with crossbow. Found in outposts and raids.</p>
</div>
</div>
</div>

<div id="passive" class="tab-content">
<div class="grid-4">
<div class="card">
<span class="card-icon">🐄</span>
<h3>Cow</h3>
<p>Provides milk, leather, and beef. Can be bred with wheat.</p>
</div>
<div class="card">
<span class="card-icon">🐖</span>
<h3>Pig</h3>
<p>Source of porkchops. Can be ridden with saddle and carrot on stick.</p>
</div>
<div class="card">
<span class="card-icon">🐔</span>
<h3>Chicken</h3>
<p>Lays eggs and provides feathers and chicken meat. Bred with seeds.</p>
</div>
<div class="card">
<span class="card-icon">🐑</span>
<h3>Sheep</h3>
<p>Provides wool and mutton. Can be dyed 16 different colors.</p>
</div>
<div class="card">
<span class="card-icon">🐰</span>
<h3>Rabbit</h3>
<p>Small hopping creature. Drops rabbit hide and meat.</p>
</div>
<div class="card">
<span class="card-icon">🐴</span>
<h3>Horse</h3>
<p>Can be tamed and ridden. Use saddle for control.</p>
</div>
<div class="card">
<span class="card-icon">🐱</span>
<h3>Cat</h3>
<p>Tamed with raw fish. Scares away creepers and phantoms.</p>
</div>
<div class="card">
<span class="card-icon">🦜</span>
<h3>Parrot</h3>
<p>Colorful bird that can sit on shoulders. Mimics nearby mob sounds.</p>
</div>
</div>
</div>

<div id="neutral" class="tab-content">
<div class="grid-4">
<div class="card">
<span class="card-icon">🐺</span>
<h3>Wolf</h3>
<p>Tamed with bones. Becomes loyal companion and protects owner.</p>
</div>
<div class="card">
<span class="card-icon">🐝</span>
<h3>Bee</h3>
<p>Pollinates crops. Produces honey. Attacks if provoked or hive damaged.</p>
</div>
<div class="card">
<span class="card-icon">🐻</span>
<h3>Polar Bear</h3>
<p>Neutral unless cubs are nearby. Very strong attack.</p>
</div>
<div class="card">
<span class="card-icon">🐬</span>
<h3>Dolphin</h3>
<p>Playful ocean mob. Gives speed boost when swimming nearby.</p>
</div>
<div class="card">
<span class="card-icon">🐼</span>
<h3>Panda</h3>
<p>Bamboo jungle dweller. Passive but protects babies.</p>
</div>
<div class="card">
<span class="card-icon">🦙</span>
<h3>Llama</h3>
<p>Pack animal that can carry chests. Spits at threats.</p>
</div>
<div class="card">
<span class="card-icon">🐐</span>
<h3>Goat</h3>
<p>Mountain mob that rams targets. Can jump very high.</p>
</div>
<div class="card">
<span class="card-icon">🦊</span>
<h3>Fox</h3>
<p>Hunts chickens and rabbits. Can pick up items in mouth.</p>
</div>
</div>
</div>

<div id="bosses" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">🐉</span>
<h3>Ender Dragon</h3>
<p>
The ultimate boss of Minecraft. Found in The End dimension. Shoots projectiles, 
heals from End Crystals. Defeating it opens the End Gateway and credits.
</p>
<span class="badge">FINAL BOSS</span>
</div>
<div class="card">
<span class="card-icon">💀</span>
<h3>Wither</h3>
<p>
Player-summoned boss. Spawned with soul sand and wither skeleton skulls. 
Shoots explosive skulls, causes Wither effect. Drops nether star for beacon.
</p>
<span class="badge">CREATED BOSS</span>
</div>
<div class="card">
<span class="card-icon">🏛️</span>
<h3>Elder Guardian</h3>
<p>
Mini-boss in ocean monuments. Inflicts Mining Fatigue effect. 
Three per monument. Drops prismarine shards and wet sponges.
</p>
<span class="badge">OCEAN BOSS</span>
</div>
<div class="card">
<span class="card-icon">⚔️</span>
<h3>Warden</h3>
<p>
Most powerful mob in Minecraft. Blind but uses sound/vibration detection. 
Found in Deep Dark biome. Extreme damage, better to sneak past it!
</p>
<span class="badge">STRONGEST</span>
</div>
</div>
</div>

</div>
</section>

<!-- BIOMES -->
<section id="biomes" class="section section-alt">
<div class="container">
<div class="section-head">
<h2>🌍 BIOMES & DIMENSIONS</h2>
<p>Discover diverse environments across three unique dimensions</p>
</div>

<div class="tabs">
<button class="tab-btn active" onclick="switchTab('overworld')">Overworld</button>
<button class="tab-btn" onclick="switchTab('nether')">The Nether</button>
<button class="tab-btn" onclick="switchTab('end')">The End</button>
</div>

<div id="overworld" class="tab-content active">
<div class="grid-4">
<div class="card">
<span class="card-icon">🌲</span>
<h3>Forest</h3>
<p>Oak and birch trees, flowers, wolves. Great for wood gathering.</p>
</div>
<div class="card">
<span class="card-icon">🏔️</span>
<h3>Mountains</h3>
<p>Tall peaks, snow, stone, emerald ore. Beautiful views.</p>
</div>
<div class="card">
<span class="card-icon">🏜️</span>
<h3>Desert</h3>
<p>Sand, cacti, temples, villages. Hot and dry climate.</p>
</div>
<div class="card">
<span class="card-icon">🌴</span>
<h3>Jungle</h3>
<p>Dense trees, cocoa beans, temples, parrots, pandas.</p>
</div>
<div class="card">
<span class="card-icon">🌊</span>
<h3>Ocean</h3>
<p>Deep water, shipwrecks, monuments, dolphins, fish.</p>
</div>
<div class="card">
<span class="card-icon">🌾</span>
<h3>Plains</h3>
<p>Flat grass, villages, horses. Perfect for building.</p>
</div>
<div class="card">
<span class="card-icon">🌿</span>
<h3>Swamp</h3>
<p>Water, slimes, witch huts, lily pads, vines.</p>
</div>
<div class="card">
<span class="card-icon">❄️</span>
<h3>Taiga</h3>
<p>Spruce trees, snow, wolves, foxes. Cold climate.</p>
</div>
<div class="card">
<span class="card-icon">🍄</span>
<h3>Mushroom Fields</h3>
<p>Giant mushrooms, mycelium, mooshrooms. Very rare!</p>
</div>
<div class="card">
<span class="card-icon">🏖️</span>
<h3>Beach</h3>
<p>Sand borders oceans. Sugar cane, turtles, shipwrecks.</p>
</div>
<div class="card">
<span class="card-icon">🌸</span>
<h3>Flower Forest</h3>
<p>Dense flowers and trees. Bees and beautiful scenery.</p>
</div>
<div class="card">
<span class="card-icon">🏔️</span>
<h3>Ice Spikes</h3>
<p>Frozen spikes of ice. Rare and stunning biome.</p>
</div>
</div>
</div>

<div id="nether" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">🔥</span>
<h3>Nether Wastes</h3>
<p>
Classic Nether biome. Netherrack, lava seas, ghasts, and zombie piglin. 
Source of quartz and glowstone.
</p>
</div>
<div class="card">
<span class="card-icon">🌳</span>
<h3>Warped Forest</h3>
<p>
Cyan forest with warped fungi. Endermen spawn here. Relatively safe Nether biome.
</p>
</div>
<div class="card">
<span class="card-icon">🍄</span>
<h3>Crimson Forest</h3>
<p>
Red forest with crimson fungi. Hoglins and piglins spawn. Dangerous but rich in resources.
</p>
</div>
<div class="card">
<span class="card-icon">⛏️</span>
<h3>Basalt Deltas</h3>
<p>
Volcanic biome with basalt pillars and magma cubes. Difficult terrain to navigate.
</p>
</div>
<div class="card">
<span class="card-icon">🏰</span>
<h3>Soul Sand Valley</h3>
<p>
Haunting blue biome with soul sand and soul soil. Skeletons and ghasts everywhere.
</p>
</div>
<div class="card">
<span class="card-icon">🏛️</span>
<h3>Nether Fortress</h3>
<p>
Structure with blazes and wither skeletons. Essential for blaze rods and wither skulls.
</p>
</div>
</div>
</div>

<div id="end" class="tab-content">
<div class="grid-2">
<div class="card">
<span class="card-icon">🌑</span>
<h3>The End</h3>
<p>
Void dimension with floating islands. Home of the Ender Dragon. 
End stone and obsidian pillars everywhere.
</p>
</div>
<div class="card">
<span class="card-icon">🏝️</span>
<h3>Outer End Islands</h3>
<p>
Islands beyond the main End. End cities, chorus plants, and shulkers. 
Find elytra wings here!
</p>
</div>
<div class="card">
<span class="card-icon">🏰</span>
<h3>End City</h3>
<p>
Tall structures made of purpur blocks. Contains valuable loot and shulker boxes. 
Guarded by shulkers.
</p>
</div>
<div class="card">
<span class="card-icon">🚀</span>
<h3>End Ship</h3>
<p>
Rare floating ship structure. Contains elytra wings and dragon head. 
The ultimate prize of The End!
</p>
</div>
</div>
</div>

</div>
</section>

<!-- BLOCKS & MATERIALS -->
<section id="blocks" class="section">
<div class="container">
<div class="section-head">
<h2>🧱 BLOCKS & MATERIALS</h2>
<p>Building blocks, ores, and special materials</p>
</div>

<div class="tabs">
<button class="tab-btn active" onclick="switchTab('natural')">Natural Blocks</button>
<button class="tab-btn" onclick="switchTab('ores')">Ores & Minerals</button>
<button class="tab-btn" onclick="switchTab('manufactured')">Manufactured</button>
<button class="tab-btn" onclick="switchTab('special')">Special Blocks</button>
</div>

<div id="natural" class="tab-content active">
<div class="grid-4">
<div class="card">
<span class="card-icon">🟫</span>
<h3>Dirt</h3>
<p>Most common block. Turns to grass with light exposure.</p>
</div>
<div class="card">
<span class="card-icon">🟩</span>
<h3>Grass Block</h3>
<p>Dirt with grass on top. Base of most biomes.</p>
</div>
<div class="card">
<span class="card-icon">⬜</span>
<h3>Stone</h3>
<p>Most abundant underground block. Base building material.</p>
</div>
<div class="card">
<span class="card-icon">🪨</span>
<h3>Cobblestone</h3>
<p>Dropped when stone is mined. Used in basic crafting.</p>
</div>
<div class="card">
<span class="card-icon">🪵</span>
<h3>Wood Logs</h3>
<p>From trees. Essential for crafting and building.</p>
</div>
<div class="card">
<span class="card-icon">🟨</span>
<h3>Sand</h3>
<p>Found in deserts and beaches. Makes glass when smelted.</p>
</div>
<div class="card">
<span class="card-icon">🟧</span>
<h3>Sandstone</h3>
<p>Compressed sand. Decorative desert material.</p>
</div>
<div class="card">
<span class="card-icon">🪨</span>
<h3>Gravel</h3>
<p>Falls when unsupported. Source of flint.</p>
</div>
</div>
</div>

<div id="ores" class="tab-content">
<div class="grid-4">
<div class="card">
<span class="card-icon">⚫</span>
<h3>Coal Ore</h3>
<p>Fuel and torches. Very common at all depths.</p>
</div>
<div class="card">
<span class="card-icon">🟫</span>
<h3>Copper Ore</h3>
<p>Makes copper blocks. Oxidizes over time to green.</p>
</div>
<div class="card">
<span class="card-icon">⚪</span>
<h3>Iron Ore</h3>
<p>Essential for tools, armor, and mechanisms.</p>
</div>
<div class="card">
<span class="card-icon">🟡</span>
<h3>Gold Ore</h3>
<p>Makes gold tools and powered rails. Found deep.</p>
</div>
<div class="card">
<span class="card-icon">🔷</span>
<h3>Diamond Ore</h3>
<p>Strongest vanilla ore. Makes best tools and armor.</p>
</div>
<div class="card">
<span class="card-icon">🟢</span>
<h3>Emerald Ore</h3>
<p>Rarest ore. Only in mountains. Used for trading.</p>
</div>
<div class="card">
<span class="card-icon">🔴</span>
<h3>Redstone Ore</h3>
<p>Powers machines and circuits. Glows when stepped on.</p>
</div>
<div class="card">
<span class="card-icon">🔵</span>
<h3>Lapis Lazuli</h3>
<p>Blue dye and enchanting component.</p>
</div>
<div class="card">
<span class="card-icon">🟣</span>
<h3>Ancient Debris</h3>
<p>Nether ore. Smelts to netherite scrap. Extremely rare!</p>
</div>
<div class="card">
<span class="card-icon">⬛</span>
<h3>Netherite</h3>
<p>Strongest material. Upgrade from diamond. Fire-proof!</p>
</div>
</div>
</div>

<div id="manufactured" class="tab-content">
<div class="grid-4">
<div class="card">
<span class="card-icon">🟦</span>
<h3>Glass</h3>
<p>Transparent block. Made from smelting sand.</p>
</div>
<div class="card">
<span class="card-icon">🧱</span>
<h3>Bricks</h3>
<p>Decorative block made from clay.</p>
</div>
<div class="card">
<span class="card-icon">🟥</span>
<h3>Concrete</h3>
<p>Solid colored blocks. 16 colors available.</p>
</div>
<div class="card">
<span class="card-icon">🟧</span>
<h3>Terracotta</h3>
<p>Colored clay. Great for building details.</p>
</div>
<div class="card">
<span class="card-icon">🟪</span>
<h3>Purpur</h3>
<p>End dimension block. Made from chorus fruit.</p>
</div>
<div class="card">
<span class="card-icon">⬜</span>
<h3>Quartz</h3>
<p>Clean white block from Nether quartz.</p>
</div>
<div class="card">
<span class="card-icon">🟫</span>
<h3>Planks</h3>
<p>Wood blocks. 9 different types from tree species.</p>
</div>
<div class="card">
<span class="card-icon">💎</span>
<h3>Block of Diamond</h3>
<p>Storage and decoration. 9 diamonds compressed.</p>
</div>
</div>
</div>

<div id="special" class="tab-content">
<div class="grid-4">
<div class="card">
<span class="card-icon">📦</span>
<h3>Chest</h3>
<p>Storage container. Double chest holds 54 stacks.</p>
</div>
<div class="card">
<span class="card-icon">🔥</span>
<h3>Furnace</h3>
<p>Smelts ores and cooks food using fuel.</p>
</div>
<div class="card">
<span class="card-icon">🛠️</span>
<h3>Crafting Table</h3>
<p>3x3 crafting grid. Essential for most recipes.</p>
</div>
<div class="card">
<span class="card-icon">🛏️</span>
<h3>Bed</h3>
<p>Sets spawn point and skips night. 16 colors.</p>
</div>
<div class="card">
<span class="card-icon">🔮</span>
<h3>Enchanting Table</h3>
<p>Adds magical enhancements to gear using XP.</p>
</div>
<div class="card">
<span class="card-icon">⚗️</span>
<h3>Brewing Stand</h3>
<p>Creates potions with various effects.</p>
</div>
<div class="card">
<span class="card-icon">💡</span>
<h3>Beacon</h3>
<p>Gives powerful buffs. Requires nether star.</p>
</div>
<div class="card">
<span class="card-icon">🌀</span>
<h3>Portal</h3>
<p>Nether and End portals for dimension travel.</p>
</div>
<div class="card">
<span class="card-icon">📝</span>
<h3>Command Block</h3>
<p>Executes commands. Creative/operator only.</p>
</div>
<div class="card">
<span class="card-icon">🎵</span>
<h3>Note Block</h3>
<p>Plays musical notes. Create songs!</p>
</div>
<div class="card">
<span class="card-icon">🪴</span>
<h3>Composter</h3>
<p>Converts plant material into bone meal.</p>
</div>
<div class="card">
<span class="card-icon">🔔</span>
<h3>Bell</h3>
<p>Village centerpiece. Alerts villagers to raids.</p>
</div>
</div>
</div>

</div>
</section>

<!-- STATS -->
<section class="section section-alt">
<div class="container">
<div class="section-head">
<h2>📊 MINECRAFT BY THE NUMBERS</h2>
</div>

<div class="stats">
<div class="stat">
<span class="stat-value">238+</span>
<span class="stat-label">Unique Mobs</span>
</div>
<div class="stat">
<span class="stat-value">60+</span>
<span class="stat-label">Biomes</span>
</div>
<div class="stat">
<span class="stat-value">800+</span>
<span class="stat-label">Block Types</span>
</div>
<div class="stat">
<span class="stat-value">400+</span>
<span class="stat-label">Crafting Recipes</span>
</div>
<div class="stat">
<span class="stat-value">3</span>
<span class="stat-label">Dimensions</span>
</div>
<div class="stat">
<span class="stat-value">140M+</span>
<span class="stat-label">Monthly Players</span>
</div>
</div>
</div>
</section>

</main>

<footer>
<div class="container">
<div style="font-size:28px;font-weight:bold;color:var(--grass)">⛏️ MINECRAFT UNIVERSE</div>
<p>Your complete guide to Minecraft game modes, features, mobs, biomes, and blocks.</p>
<p>© 2024 Minecraft Universe • Educational Fan Resource</p>
<p style="font-size:11px;margin-top:15px">
This is an unofficial fan-made resource. Minecraft is a trademark of Mojang Studios.
</p>
</div>
</footer>

<script>
// Tab switching system
function switchTab(tabName){
    // Remove all active states
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
    
    // Add active to clicked tab button
    event.target.classList.add('active');
    
    // Show corresponding content
    const content = document.getElementById(tabName);
    if(content) content.classList.add('active');
}

// Smooth scroll function
function scrollTo(target){
    const element = document.querySelector(target);
    if(element){
        element.scrollIntoView({behavior:'smooth'});
    }
}

// Random Minecraft facts
const facts = [
    "💎 Diamonds are most common at Y-level -59!",
    "🐷 The Creeper was created by accident - it was meant to be a pig!",
    "🌍 A Minecraft world is 8 times the surface area of Earth!",
    "⚡ Redstone was inspired by electrical circuits!",
    "🐉 The Ender Dragon is named Jean!",
    "🎵 The iconic soundtrack was composed by C418!",
    "🍄 Mushroom biomes have no hostile mob spawns!",
    "🔥 Netherite doesn't burn in lava!",
    "🏔️ The build height is 320 blocks (Y-level -64 to 256)!",
    "🐝 Bees can help your crops grow faster!",
    "⛏️ A diamond pickaxe can mine 1562 blocks!",
    "🌳 There are 9 different wood types in Minecraft!",
    "💀 The Wither can break obsidian with its attacks!",
    "🎮 Minecraft is the best-selling video game of all time!",
    "🌙 Phantoms only spawn if you haven't slept in 3+ days!",
    "🔔 Ringing a bell makes villagers go indoors!",
    "🐺 Tamed wolves have a collar that can be dyed 16 colors!",
    "🏹 Infinity bow enchantment still requires 1 arrow in inventory!",
    "🧟 Baby zombie villagers can be cured with weakness potion and golden apple!",
    "🌊 Dolphins can lead you to treasure if you feed them fish!"
];

function randomFact(){
    const fact = facts[Math.floor(Math.random() * facts.length)];
    alert(fact);
}

// Initialize
console.log('⛏️ Minecraft Universe loaded!');
</script>

</body>
</html>
"""

@app.route('/')
def home():
    """Main page with full Minecraft universe"""
    return render_template_string(HTML)

@app.route('/api/stats')
def stats():
    """API endpoint for Minecraft statistics"""
    return jsonify({
        "game_modes": 5,
        "mobs": 238,
        "biomes": 60,
        "blocks": 800,
        "dimensions": 3,
        "monthly_players": "140M+",
        "status": "active"
    })

@app.route('/api/random-fact')
def random_fact():
    """Get a random Minecraft fact"""
    facts = [
        "Diamonds are most common at Y-level -59",
        "The Creeper was created by accident",
        "Minecraft worlds are 8x Earth's surface area",
        "The Ender Dragon's name is Jean",
        "Netherite doesn't burn in lava",
        "Mushroom biomes have no hostile mob spawns"
    ]
    return jsonify({
        "fact": random.choice(facts),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/game-modes')
def game_modes():
    """API endpoint for game mode information"""
    return jsonify({
        "modes": [
            {
                "name": "Survival",
                "icon": "⚔️",
                "description": "Gather resources, craft, build, and survive against mobs",
                "features": ["Health/hunger management", "Resource gathering", "Mob combat", "Crafting system"],
                "difficulty": "Medium to Hard"
            },
            {
                "name": "Creative",
                "icon": "🎨",
                "description": "Unlimited resources and flying for pure building creativity",
                "features": ["Unlimited blocks", "Flying", "No health/hunger", "Instant mining"],
                "difficulty": "None"
            },
            {
                "name": "Adventure",
                "icon": "🗺️",
                "description": "Designed for custom maps with restricted block breaking",
                "features": ["Custom map support", "Restricted mining", "Quest-based gameplay"],
                "difficulty": "Varies"
            },
            {
                "name": "Spectator",
                "icon": "👻",
                "description": "Observe the world without interaction, fly through blocks",
                "features": ["Invisible to mobs", "Fly through blocks", "View from mob perspective"],
                "difficulty": "None"
            },
            {
                "name": "Hardcore",
                "icon": "💀",
                "description": "Survival with permanent death and locked difficulty",
                "features": ["One life only", "Maximum difficulty", "Permadeath", "No respawning"],
                "difficulty": "Extreme"
            }
        ]
    })

@app.route('/api/mobs/<category>')
def mobs_by_category(category):
    """Get mobs by category (hostile, passive, neutral, bosses)"""
    mobs_data = {
        "hostile": [
            {"name": "Zombie", "icon": "🧟", "drops": ["Rotten Flesh", "Iron Ingot (rare)"]},
            {"name": "Skeleton", "icon": "💀", "drops": ["Bone", "Arrow"]},
            {"name": "Creeper", "icon": "💥", "drops": ["Gunpowder"]},
            {"name": "Spider", "icon": "🕷️", "drops": ["String", "Spider Eye"]},
            {"name": "Enderman", "icon": "👁️", "drops": ["Ender Pearl"]},
        ],
        "passive": [
            {"name": "Cow", "icon": "🐄", "drops": ["Beef", "Leather"]},
            {"name": "Pig", "icon": "🐖", "drops": ["Porkchop"]},
            {"name": "Chicken", "icon": "🐔", "drops": ["Chicken", "Feather", "Egg"]},
            {"name": "Sheep", "icon": "🐑", "drops": ["Wool", "Mutton"]},
        ],
        "neutral": [
            {"name": "Wolf", "icon": "🐺", "drops": ["Can be tamed"]},
            {"name": "Bee", "icon": "🐝", "drops": ["Honey", "Honeycomb"]},
            {"name": "Dolphin", "icon": "🐬", "drops": ["Cod (raw)"]},
        ],
        "bosses": [
            {"name": "Ender Dragon", "icon": "🐉", "drops": ["Dragon Egg", "XP"], "difficulty": "Hard"},
            {"name": "Wither", "icon": "💀", "drops": ["Nether Star"], "difficulty": "Very Hard"},
            {"name": "Warden", "icon": "⚔️", "drops": ["Sculk Catalyst"], "difficulty": "Extreme"},
        ]
    }
    
    return jsonify({
        "category": category,
        "mobs": mobs_data.get(category, [])
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Minecraft Universe API",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
