let liveLabels = [];
let liveData = [];
let currentExercise = "{{ exercise }}";  // track selected exercise

const ctx = document.getElementById('liveChart').getContext('2d');
const liveChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: liveLabels,
        datasets: [{
            label: currentExercise + ' Reps',
            data: liveData,
            borderColor: 'rgba(56, 189, 248,1)',
            backgroundColor: 'rgba(56, 189, 248,0.2)',
            tension: 0.3
        }]
    },
    options: { responsive: true }
});

function fetchStats() {
    fetch("/get_live_stats")
        .then(res => res.json())
        .then(data => {
            const now = new Date().toLocaleTimeString();
            liveLabels.push(now);
            liveData.push(data.count);

            // Keep only last 20 points
            if(liveLabels.length > 20){
                liveLabels.shift();
                liveData.shift();
            }

            liveChart.update();
        });
}

// Fetch live stats every second
setInterval(fetchStats, 1000);

function changeExercise(ex) {
    fetch("/set_exercise", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({exercise: ex})
    }).then(() => {
        // Reset chart data for new exercise
        liveLabels = [];
        liveData = [];
        currentExercise = ex;

        liveChart.data.labels = liveLabels;
        liveChart.data.datasets[0].data = liveData;
        liveChart.data.datasets[0].label = ex + ' Reps';
        liveChart.update();
    });
}

function saveSession() {
    fetch("/save_session", {method: "POST"})
    alert("Session saved to CSV!")
}