async def create_enrich_policy(es, params):
    await es.enrich.put_policy(
        name=params["policy-id"],
        body=params["body"]
    )

async def delete_enrich_policy(es, params):
    await es.enrich.delete_policy(
        name=params["policy-id"],
        ignore=[404]
    )

async def execute_enrich_policy(es, params):
    import elasticsearch
    execute_response = await es.enrich.execute_policy(
        name=params["policy-id"],
        wait_for_completion=False
    )
    print(execute_response)
    completed = False
    while not completed:
        try:
            task_response = await es.tasks.get(task_id=execute_response["task"])
            completed = task_response["completed"] == "true"
        except elasticsearch.TransportError as error:
            if error.status_code == 404:
                return
            raise

async def delete_pipeline(es, params):
    await es.ingest.delete_pipeline(
        id=params["id"],
        ignore=[404]
    )

def register(registry):
    registry.register_runner("create-enrich-policy", create_enrich_policy, async_runner=True)
    registry.register_runner("execute-enrich-policy", execute_enrich_policy, async_runner=True)
    registry.register_runner("delete-pipeline", delete_pipeline, async_runner=True)
    registry.register_runner("delete-enrich-policy", delete_enrich_policy, async_runner=True)