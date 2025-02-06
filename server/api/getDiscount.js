export default defineEventHandler(async (event) => {
    const query = getQuery(event);
    var offerUid = query.offerUid;

    const url = `https://test.tzpro.xyz/api?page=1`
    const result = await fetch(url);
    const decodedResult = await result.json()
    var hitList = decodedResult.hits;

    var numberOfPages = decodedResult.nbPages;

    for (let i = 2; i <= numberOfPages; i++) {
        const url = `https://test.tzpro.xyz/api?page=${i}`;
        const result = await fetch(url);
        const decodedResult = await result.json()


        hitList = hitList.concat(decodedResult.hits);
    }

    for (let i = 0; i < hitList.length; i++) {
        if (hitList[i].offerUid == offerUid) {
            return hitList[i];
        }
    }

})
