SELECT owner.owner_id, owner_name, count(DISTINCT cam.category_id) AS different_category_count
FROM owner
LEFT JOIN article
    ON owner.owner_id = article.owner_id
LEFT JOIN category_article_mapping cam
    ON article.article_id = cam.article_id
GROUP BY owner.owner_id
ORDER BY different_category_count DESC
;