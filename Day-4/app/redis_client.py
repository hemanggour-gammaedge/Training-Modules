from redis import Redis

cache_client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

