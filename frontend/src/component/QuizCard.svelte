<script>
    export let quiz = {
        name: "Default value",
        id: 0,
        questions: [0, 1, 2],
    };
</script>

<article>
    <h3>{quiz.name}</h3>
    <p>There are {quiz?.questions?.length ?? 0} questions in this quiz!</p>
</article>

<style>
    article {
        width: max(80%, 420px);
        padding: 10px 15px;
        margin: 5px auto;
        background-color: white;
        border-radius: 15px;
        box-shadow: 5px 5px 5px #000;
    }
</style>
