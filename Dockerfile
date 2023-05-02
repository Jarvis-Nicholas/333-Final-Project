#Command line to run DOCKER_BUILDKIT=0 docker build .

FROM python:3


ADD main.py .
ADD poke_center.py .
ADD pokemon_owner.py .
ADD pokemon_trainer.py .
ADD pokemon.py .
ADD pokemon_list.txt .
ADD research_lab.py .
ADD battle_stadium.py .

# Test files
ADD test_battle_stadium.py .
ADD test_poke_center.py .
ADD test_pokemon_owner_AND_pokemon.py .
ADD test_pokemon_owner.py .
ADD test_pokemon_trainer.py .
ADD test_pokemon.py .
ADD test_research_lab.py .



CMD ["python3", "./main.py"]