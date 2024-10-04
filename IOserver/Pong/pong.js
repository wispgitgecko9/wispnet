const canvas = document.getElementById("pongCanvas");
const ctx = canvas.getContext("2d");

const paddleWidth = 10;
const paddleHeight = 100;
const ballRadius = 8;

let isPaused = true;
let playerScore = 0;
let computerScore = 0;
let ballSpeed = 3; // Initial ball speed
let computerPaddleSpeed = 2; // Initial computer paddle speed



// Player Paddle
const player = {
    x: 0, 
    y: canvas.height / 2 - paddleHeight / 2, 
    width: paddleWidth, 
    height: paddleHeight, 
    dy: 7
};

// Computer Paddle
const computer = {
    x: canvas.width - paddleWidth,
    y: canvas.height / 2 - paddleHeight / 2, 
    width: paddleWidth, 
    height: paddleHeight,
    dy: 4
};

// Ball
const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    dx: 3, 
    dy: 3
};

// Draw paddles and ball
function drawPaddle(paddle) {
    ctx.fillStyle = "#f4f4f4";
    ctx.fillRect(paddle.x, paddle.y, paddle.width, paddle.height);
}

function drawBall() {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = "#4CAF50";
    ctx.fill();
    ctx.closePath();
}

// Move player paddle with keyboard
document.addEventListener("keydown", movePlayerPaddle);

function movePlayerPaddle(e) {
    if (e.key === "ArrowUp" && player.y > 0) {
        player.y -= player.dy;
    } else if (e.key === "ArrowDown" && player.y < canvas.height - paddleHeight) {
        player.y += player.dy;
    }
}

// Computer paddle movement
function moveComputerPaddle() {
    if (ball.y < computer.y + computer.height / 2 && computer.y > 0) {
        computer.y -= computerPaddleSpeed;  // Use computerPaddleSpeed
    } else if (ball.y > computer.y + computer.height / 2 && computer.y < canvas.height - paddleHeight) {
        computer.y += computerPaddleSpeed;  // Use computerPaddleSpeed
    }
}

// Ball movement and collision with walls/paddles
function moveBall() {
    ball.x += ball.dx * ballSpeed;  // Use ballSpeed to control speed
    ball.y += ball.dy * ballSpeed;

    // Wall collision (top and bottom)
    if (ball.y + ballRadius > canvas.height || ball.y - ballRadius < 0) {
        ball.dy = -ball.dy;
    }

    // Paddle collision
    if (ball.x - ballRadius < player.x + paddleWidth && ball.y > player.y && ball.y < player.y + paddleHeight) {
        ball.dx = -ball.dx;
    } else if (ball.x + ballRadius > computer.x && ball.y > computer.y && ball.y < computer.y + paddleHeight) {
        ball.dx = -ball.dx;
    }

    // Score and reset ball if it goes out of bounds
    if (ball.x + ballRadius < 0) {
        computerScore++;
        updateScore();
        resetBall();
    } else if (ball.x - ballRadius > canvas.width) {
        playerScore++;
        updateScore();
        resetBall();
    }
}


    // Score and reset ball if it goes out of bounds
    if (ball.x + ballRadius < 0) {
        computerScore++;
        updateScore();
        resetBall();
    } else if (ball.x - ballRadius > canvas.width) {
        playerScore++;
        updateScore();
        resetBall();
    }

// Reset ball position
function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;

    // Randomize direction
    ball.dx = ball.dx > 0 ? ballSpeed : -ballSpeed;
    ball.dy = Math.random() > 0.5 ? ballSpeed : -ballSpeed;
}

// Update the score display
function updateScore() {
    document.getElementById('playerScore').innerText = playerScore;
    document.getElementById('computerScore').innerText = computerScore;
}

function setEasyLevel() {
    ballSpeed = 2;  // Slower ball
    computerPaddleSpeed = 1.5;  // Slower computer paddle
}

function setMediumLevel() {
    ballSpeed = 3;  // Default ball speed
    computerPaddleSpeed = 2;  // Default computer paddle speed
    
}

function setHardLevel() {
    ballSpeed = 4;  // Faster ball
    computerPaddleSpeed = 3;  // Faster computer paddle
}

function resetGame() {
    playerScore = 0;
    computerScore = 0;
    updateScore();
    resetBall(); // Reset ball position and direction
}

// Start and pause functionality
document.getElementById("startBtn").addEventListener("click", function() {
    isPaused = false;
});

document.getElementById("pauseBtn").addEventListener("click", function() {
    isPaused = true;
});

document.getElementById("easyBtn").addEventListener("click", function() {
    setEasyLevel();
    resetGame();  // Optional: reset the game when a new level is selected
});

document.getElementById("mediumBtn").addEventListener("click", function() {
    setMediumLevel();
    resetGame();
});

document.getElementById("hardBtn").addEventListener("click", function() {
    setHardLevel();
    resetGame();
});

// Game loop
function gameLoop() {
    if (!isPaused) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        drawPaddle(player);
        drawPaddle(computer);
        drawBall();

        moveBall();
        moveComputerPaddle();
    }

    requestAnimationFrame(gameLoop);
}

gameLoop();
