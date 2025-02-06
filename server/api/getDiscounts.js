export default defineEventHandler(async (event) => {
    const query = getQuery(event);
    const url = `https://test.tzpro.xyz/api?page=${query.page}`
    const result = await fetch(url);

    return await result.json()

})
