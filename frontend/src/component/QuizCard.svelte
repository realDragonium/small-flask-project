<script>
    export let quiz = {
        name: "Best quiz",
        id: 0,
        questions: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    };
</script>

<article>
    <h3>{quiz.name}</h3>
    <p>There are {quiz.questions?.length ?? 0} questions in this quiz!</p>
</article>

<style>
</style>
