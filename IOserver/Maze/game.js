// game.js
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const levels =  [
    [
        '#############',
        '#S#.........#',
        '#.#.#######.#',
        '#.#.#.....#.#',
        '#.#.#.###.#.#',
        '#.#.#.#.#.#.#',
        '#...#.#.#.#.#',
        '###.#.#.#.#.#',
        '#E..#.......#',
        '#############',
    ],
    // Add more levels here
    [
        '#############',
        '#S#.........#',
        '#.#.#######.#',
        '#.#.#.....#.#',
        '#.#.#.###.#.#',
        '#.#.#.#.#.#.#',
        '#...#.#...#.#',
        '#.#.#.#.###.#',
        '#...#.......#',
        '#####E#######',
    ],
  [
        '#############',
        '#S#.........#',
        '#.#.##.####.#',
        '#.#.......#.#',
        '#.#.#.###.#.#',
        '#.#.#.#.#.#.#',
        '#.E.......#.#',
        '#.#.#.#.###.#',
        '#...#.......#',
        '#############',
    ],
  [
        '#############',
        '#S#.........#',
        '#.#.#######.#',
        '#.#.#.....#.#',
        '#.#.#.###.#.#',
        '#.#.#.#.#.#.#',
        '#...#.#.#.#.#',
        '#.#.#.#.#.#.#',
        '#...#.......#',
        '#####E#######',
    ],
  [
        '#############',
        '#........#..#',
        '##....#.....#',
        '#S#...E.....#',
        '#.#.........#',
        '#.........#.#',
        '#......#....#',
        '#..#........#',
        '#...........#',
        '#############',
    ],
 [
        '####################E.#..#',
        '#........#.............#.#',
        '##....#..................#',
        '#S#......................#',
        '#.#......................#',
        '#.........#..............#',
        '#......#.................#',
        '#..#.....................#',
        '#...................#....#',
        '##########################',
    ],
[
        '##########################',
        '#........................#',
        '#.#####...#...#..........#',
        '#...#.....#.#.#.....#....#',
        '#...#.....#.#.#..........#',
        '##..#.S....#.#..E........#',
        '#............#...........#',
        '#..###..#...#####.#......#',
        '#....#.#.#....#.###......#',
        '#...#..#.#...#....#......#',
        '#..###..#...###...#......#',
        '#........................#',
        '#.................#......#',
        '#....................#...#',
        '##########################',
    ],
[
        '####################E#####',
        '#S.......#.........#...#.#',
        '##....#.....#...#..#.....#',
        '#.#.......#.....#.#.....##',
        '#.#.............#...#....#',
        '#..........#...##........#',
        '#......#...#....#........#',
        '##.....#........#......#.#',
        '#......#........#........#',
        '##########################',
    ],


];

const saveButton = document.getElementById('saveButton');
if (saveButton) {
    saveButton.addEventListener('click', () => {
        saveProgress();
    });
}


let currentLevel = 0;
let player = {
    x: 30,
    y: 30,
    size: 20,
};

let score = 0;

// Load saved progress from local storage
const savedProgress = localStorage.getItem('gameProgress');
if (savedProgress) {
    const progress = JSON.parse(savedProgress);
    currentLevel = progress.currentLevel;
    player = progress.player;
    score = progress.score;
}

function drawMaze() {
    const maze = levels[currentLevel];
    for (let row = 0; row < maze.length; row++) {
        for (let col = 0; col < maze[row].length; col++) {
            if (maze[row][col] === '#') {
                ctx.fillStyle = '#000';
                ctx.fillRect(col * player.size, row * player.size, player.size, player.size);
            } else if (maze[row][col] === 'E') {
                // 'E' denotes the exit
                ctx.fillStyle = '#0F0';
                ctx.fillRect(col * player.size, row * player.size, player.size, player.size);
            }
        }
    }
}


function resetProgress() {
    // Reset saved progress in local storage
    localStorage.removeItem('gameProgress');
    alert('Progress reset! Please refresh the page.');
}

function handleInput() {
    document.addEventListener('keydown', (event) => {
        switch (event.key) {
            case 'ArrowUp':
                if (levels[currentLevel][Math.floor(player.y / player.size) - 1][Math.floor(player.x / player.size)] !== '#') {
                    player.y -= player.size;
                }
                break;
            case 'ArrowDown':
                if (levels[currentLevel][Math.floor(player.y / player.size) + 1][Math.floor(player.x / player.size)] !== '#') {
                    player.y += player.size;
                }
                break;
            case 'ArrowLeft':
                if (levels[currentLevel][Math.floor(player.y / player.size)][Math.floor(player.x / player.size) - 1] !== '#') {
                    player.x -= player.size;
                }
                break;
            case 'ArrowRight':
                if (levels[currentLevel][Math.floor(player.y / player.size)][Math.floor(player.x / player.size) + 1] !== '#') {
                    player.x += player.size;
                }
                break;
        }

        // Check if the player reached the exit
        if (levels[currentLevel][Math.floor(player.y / player.size)][Math.floor(player.x / player.size)] === 'E') {
            score += 10; // Increase score when reaching the exit
            updateScoreboard();
            nextLevel();
            saveProgress(); // Save progress after reaching the exit
        }
    });
}

function nextLevel() {
     if (currentLevel < levels.length - 1) {
        currentLevel++;
        resetPlayerPosition();
    } else {
        // Optionally, handle game completion
        console.log('Game Completed!');
}
}{}

function resetPlayerPosition() {
      player.x = 30;
    player.y = 30;
}

function update() {
    // ... (unchanged)
}

function draw() {
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw maze
    drawMaze();

    // Draw player
    ctx.fillStyle = '#00F';
    ctx.fillRect(player.x, player.y, player.size, player.size);

    // Draw scoreboard
    ctx.fillStyle = '#000';
    ctx.font = '16px Arial';
    ctx.fillText('Score: ' + score, 10, 20);
}

function updateScoreboard() {
    // Update the scoreboard on the screen
    const scoreboardElement = document.getElementById('scoreboard');
    if (scoreboardElement) {
        scoreboardElement.textContent = 'Score: ' + score;
    }
}

function saveProgress() {
    // Save current game progress to local storage
    const progress = {
        currentLevel,
        player,
        score,
    };
    localStorage.setItem('gameProgress', JSON.stringify(progress));
}

function gameLoop() {
    handleInput();
    update();
    draw();
    requestAnimationFrame(gameLoop);
}


function resetProgress() {
    // Reset saved progress in local storage
    localStorage.removeItem('gameProgress');
    alert('Progress reset! Please refresh the page.');
}


// Start the game loop
gameLoop();

