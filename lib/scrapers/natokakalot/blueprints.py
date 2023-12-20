mangas_blueprint = {
    "mangas": {
        "parent_selector": ".content-genres-item",
        "children": { 
            "manga_slug": {
                "selector": ".genres-item-img.bookmark_check",
                "attributes": {
                    "slug": "href",
                }
            },
        }
    },
}
chapters_blueprint = {
    # "mangas": {
    #     "parent_selector": ".panel-content-genres",
    #     "children": { 
    #         "manga_slug": {
    #             "selector": ".genres-item-img.bookmark_check",
    #             "attributes": {
    #                 "slug": "href",
    #             }
    #         },
    #     }
    # },
}