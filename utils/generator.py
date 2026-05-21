import random


TOPIC_KNOWLEDGE = {
    "photosynthesis": {
        "display": "Photosynthesis",
        "definition": "Photosynthesis is the process plants use to make food using sunlight, carbon dioxide, and water.",
        "key_terms": ["sunlight", "chlorophyll", "carbon dioxide", "water", "glucose", "oxygen", "chloroplasts"],
        "important_facts": [
            "Plants absorb light energy using chlorophyll.",
            "Carbon dioxide enters the plant through tiny openings called stomata.",
            "Water is absorbed by roots and transported to leaves.",
            "Glucose is produced as food for the plant.",
            "Oxygen is released as a by-product.",
            "Photosynthesis mainly happens in chloroplasts.",
            "The process supports food chains by producing energy-rich glucose.",
        ],
        "examples": [
            "A green leaf making glucose in sunlight.",
            "Aquatic plants releasing oxygen bubbles in water.",
            "A plant growing better when it receives enough light.",
        ],
        "common_mistakes": [
            "Thinking plants get all their food from soil.",
            "Forgetting that oxygen is a by-product.",
            "Confusing photosynthesis with respiration.",
        ],
        "real_world_use": [
            "Photosynthesis supports agriculture and food production.",
            "It helps maintain oxygen levels in the atmosphere.",
            "It is important for ecosystems and climate balance.",
        ],
        "memory_tip": "Remember: light + carbon dioxide + water helps plants make glucose and oxygen.",
    },

    "python programming": {
        "display": "Python Programming",
        "definition": "Python programming is writing instructions in the Python language to solve problems or automate tasks.",
        "key_terms": ["variable", "function", "loop", "condition", "list", "dictionary", "syntax"],
        "important_facts": [
            "Variables store values for later use.",
            "Functions organize reusable blocks of code.",
            "Loops repeat actions without rewriting code.",
            "Conditions help programs make decisions.",
            "Lists store ordered collections of items.",
            "Dictionaries store key-value pairs.",
            "Indentation is important in Python syntax.",
        ],
        "examples": [
            "Using a loop to print numbers from 1 to 10.",
            "Writing a function to calculate a total.",
            "Using a list to store student names.",
        ],
        "common_mistakes": [
            "Forgetting correct indentation.",
            "Using a variable before defining it.",
            "Confusing single equals sign with double equals sign.",
        ],
        "real_world_use": [
            "Python is used in web apps, automation, data science, and AI.",
            "Python scripts can automate repetitive computer tasks.",
            "Python is popular for beginner-friendly programming education.",
        ],
        "memory_tip": "Think: variables store, functions reuse, loops repeat, conditions decide.",
    },

    "world war ii": {
        "display": "World War II",
        "definition": "World War II was a major global conflict from 1939 to 1945 involving many nations around the world.",
        "key_terms": ["Allies", "Axis Powers", "invasion", "Holocaust", "D-Day", "atomic bomb", "United Nations"],
        "important_facts": [
            "The war began in Europe after Germany invaded Poland in 1939.",
            "The main Axis powers included Germany, Italy, and Japan.",
            "The main Allied powers included Britain, the Soviet Union, the United States, and China.",
            "D-Day was a major Allied invasion of Normandy in 1944.",
            "The Holocaust was the systematic persecution and murder of millions of Jews and others.",
            "The war ended in 1945 after Germany and Japan surrendered.",
            "The United Nations was formed after the war to promote peace.",
        ],
        "examples": [
            "D-Day changed the course of the war in Western Europe.",
            "The Battle of Britain showed the importance of air power.",
            "The atomic bombings contributed to Japan's surrender.",
        ],
        "common_mistakes": [
            "Thinking the war only happened in Europe.",
            "Forgetting the Pacific theater.",
            "Confusing World War I and World War II causes.",
        ],
        "real_world_use": [
            "World War II shaped modern international relations.",
            "It led to major changes in borders, alliances, and global power.",
            "It influenced human rights discussions and international law.",
        ],
        "memory_tip": "Remember: 1939 start, 1945 end, Axis vs Allies.",
    },

    "mitochondria": {
        "display": "Mitochondria",
        "definition": "Mitochondria are cell organelles that help produce energy for the cell.",
        "key_terms": ["cell", "organelle", "ATP", "energy", "cellular respiration", "powerhouse", "glucose"],
        "important_facts": [
            "Mitochondria are often called the powerhouse of the cell.",
            "They help convert energy from food into ATP.",
            "ATP is the main energy currency of the cell.",
            "Mitochondria are involved in cellular respiration.",
            "Cells that need more energy often have more mitochondria.",
            "Mitochondria have their own DNA.",
            "They are found in most eukaryotic cells.",
        ],
        "examples": [
            "Muscle cells have many mitochondria because they need lots of energy.",
            "A cell uses ATP produced by mitochondria to perform work.",
            "Mitochondria support energy needs during exercise.",
        ],
        "common_mistakes": [
            "Thinking mitochondria create energy from nothing.",
            "Forgetting that ATP is the usable energy molecule.",
            "Confusing mitochondria with the nucleus.",
        ],
        "real_world_use": [
            "Understanding mitochondria helps explain energy use in cells.",
            "Mitochondrial problems can affect body systems that need lots of energy.",
            "They are important in biology, medicine, and exercise science.",
        ],
        "memory_tip": "Mitochondria = powerhouse because they help make ATP energy.",
    },

    "democracy": {
        "display": "Democracy",
        "definition": "Democracy is a system of government where citizens have power, often through voting and representation.",
        "key_terms": ["citizens", "voting", "rights", "representation", "elections", "majority", "constitution"],
        "important_facts": [
            "Citizens participate in democracy by voting and expressing opinions.",
            "Elections allow people to choose leaders.",
            "Democratic systems protect rights and freedoms.",
            "Representation means elected leaders speak for the people.",
            "A constitution can limit government power.",
            "Democracy depends on informed and active citizens.",
            "Free and fair elections are central to democracy.",
        ],
        "examples": [
            "Citizens voting in an election.",
            "A parliament debating laws.",
            "People peacefully expressing opinions about public issues.",
        ],
        "common_mistakes": [
            "Thinking democracy only means voting.",
            "Forgetting the importance of rights and rule of law.",
            "Confusing democracy with dictatorship.",
        ],
        "real_world_use": [
            "Democracy affects how laws are made.",
            "It gives citizens a voice in government decisions.",
            "It helps protect freedom and accountability.",
        ],
        "memory_tip": "Democracy = people power through voting, rights, and representation.",
    },
}


GENERIC_DISTRACTORS = [
    "It is unrelated to the topic.",
    "It means ignoring the main idea.",
    "It is only used for memorizing random facts.",
    "It is the opposite of the correct idea.",
    "It removes the need for practice.",
    "It is always caused by luck.",
    "It has no real-world connection.",
    "It is only useful in one situation.",
]


def _normalize_topic(topic):
    return topic.strip().lower()


def _get_knowledge(topic):
    return TOPIC_KNOWLEDGE.get(_normalize_topic(topic))


def _display_topic(topic):
    knowledge = _get_knowledge(topic)
    if knowledge:
        return knowledge["display"]
    return topic.strip().title()


def _fallback_knowledge(topic):
    display = _display_topic(topic)

    return {
        "display": display,
        "definition": f"{display} is an important study topic that can be understood by learning its meaning, key ideas, examples, and common mistakes.",
        "key_terms": ["definition", "key idea", "example", "application", "mistake", "summary", "practice"],
        "important_facts": [
            f"Start by understanding the basic definition of {display}.",
            f"Break {display} into smaller key ideas.",
            f"Use examples to understand how {display} works.",
            f"Practice explaining {display} in your own words.",
            f"Review common mistakes related to {display}.",
            f"Connect {display} to real-life situations.",
            f"Test yourself instead of only rereading notes.",
        ],
        "examples": [
            f"A simple example can make {display} easier to remember.",
            f"A real-life situation can show why {display} matters.",
            f"A practice question can check understanding of {display}.",
        ],
        "common_mistakes": [
            f"Memorizing {display} without understanding it.",
            f"Skipping examples related to {display}.",
            f"Not practicing recall after studying {display}.",
        ],
        "real_world_use": [
            f"{display} can be useful when solving problems or explaining ideas.",
            f"{display} can connect classroom learning to real situations.",
        ],
        "memory_tip": f"To remember {display}, explain it simply, use examples, and test yourself.",
    }


def _knowledge(topic):
    return _get_knowledge(topic) or _fallback_knowledge(topic)


def _difficulty_label(difficulty):
    if difficulty not in ["Beginner", "Intermediate", "Advanced"]:
        return "Beginner"
    return difficulty


def _shuffle_options(correct_answer, wrong_answers):
    clean_wrong_answers = []

    for answer in wrong_answers:
        if answer != correct_answer and answer not in clean_wrong_answers:
            clean_wrong_answers.append(answer)

    while len(clean_wrong_answers) < 3:
        extra = random.choice(GENERIC_DISTRACTORS)
        if extra != correct_answer and extra not in clean_wrong_answers:
            clean_wrong_answers.append(extra)

    options = [correct_answer] + random.sample(clean_wrong_answers, 3)
    random.shuffle(options)
    return options


class StudyMaterialGenerator:
    @staticmethod
    def generate_explanation(topic, difficulty="Beginner"):
        data = _knowledge(topic)
        difficulty = _difficulty_label(difficulty)

        if difficulty == "Beginner":
            return (
                f"{data['display']} means: {data['definition']} "
                f"A good way to begin is to remember this idea: {data['memory_tip']}"
            )

        if difficulty == "Intermediate":
            fact = random.choice(data["important_facts"])
            example = random.choice(data["examples"])
            return (
                f"{data['display']} is more than just a definition. {data['definition']} "
                f"One important point is: {fact} For example: {example}"
            )

        fact1, fact2 = random.sample(data["important_facts"], 2)
        mistake = random.choice(data["common_mistakes"])
        use = random.choice(data["real_world_use"])

        return (
            f"Advanced view of {data['display']}: {data['definition']} "
            f"Key idea 1: {fact1} Key idea 2: {fact2} "
            f"A common misconception is: {mistake} "
            f"Real-world connection: {use}"
        )

    @staticmethod
    def generate_key_points(topic, difficulty="Beginner"):
        data = _knowledge(topic)
        difficulty = _difficulty_label(difficulty)

        points = [f"Definition: {data['definition']}"]

        facts = random.sample(data["important_facts"], min(4, len(data["important_facts"])))
        points.extend(facts)

        if difficulty in ["Intermediate", "Advanced"]:
            points.append(f"Example: {random.choice(data['examples'])}")
            points.append(f"Common mistake: {random.choice(data['common_mistakes'])}")

        if difficulty == "Advanced":
            points.append(f"Real-world use: {random.choice(data['real_world_use'])}")

        return points

    @staticmethod
    def _flashcard_pool(topic, difficulty="Beginner"):
        data = _knowledge(topic)
        display = data["display"]
        difficulty = _difficulty_label(difficulty)

        pool = [
            {
                "question": f"What is the basic meaning of {display}?",
                "answer": data["definition"],
            },
            {
                "question": f"Why is {display} important to understand?",
                "answer": random.choice(data["real_world_use"]),
            },
            {
                "question": f"What is one memory tip for {display}?",
                "answer": data["memory_tip"],
            },
            {
                "question": f"What is one common mistake students make about {display}?",
                "answer": random.choice(data["common_mistakes"]),
            },
            {
                "question": f"Give one example related to {display}.",
                "answer": random.choice(data["examples"]),
            },
            {
                "question": f"What should you review first when studying {display}?",
                "answer": f"Start with the definition, then review key terms such as {', '.join(data['key_terms'][:3])}.",
            },
            {
                "question": f"How can you check if you understand {display}?",
                "answer": f"Try explaining {display} in your own words and answer practice questions without looking at notes.",
            },
            {
                "question": f"What is one important fact about {display}?",
                "answer": random.choice(data["important_facts"]),
            },
        ]

        for term in data["key_terms"]:
            pool.append(
                {
                    "question": f"Why is '{term}' connected to {display}?",
                    "answer": f"'{term}' is one of the key terms that helps explain {display}.",
                }
            )

        for fact in data["important_facts"]:
            pool.append(
                {
                    "question": f"Quick recall: what fact should you remember about {display}?",
                    "answer": fact,
                }
            )

        if difficulty in ["Intermediate", "Advanced"]:
            pool.extend(
                [
                    {
                        "question": f"How can {display} be applied in a real situation?",
                        "answer": random.choice(data["real_world_use"]),
                    },
                    {
                        "question": f"What example best helps explain {display}?",
                        "answer": random.choice(data["examples"]),
                    },
                    {
                        "question": f"How can a student avoid misunderstanding {display}?",
                        "answer": f"Avoid this mistake: {random.choice(data['common_mistakes'])}",
                    },
                ]
            )

        if difficulty == "Advanced":
            pool.extend(
                [
                    {
                        "question": f"What deeper connection can you make about {display}?",
                        "answer": f"Connect this fact to a bigger idea: {random.choice(data['important_facts'])}",
                    },
                    {
                        "question": f"What limitation or misconception should you watch for in {display}?",
                        "answer": random.choice(data["common_mistakes"]),
                    },
                    {
                        "question": f"How would you teach {display} to someone else?",
                        "answer": f"Start with: {data['definition']} Then use this example: {random.choice(data['examples'])}",
                    },
                ]
            )

        random.shuffle(pool)
        return pool

    @staticmethod
    def generate_flashcards(topic, difficulty="Beginner", num_flashcards=5):
        try:
            num_flashcards = int(num_flashcards)
        except Exception:
            num_flashcards = 5

        num_flashcards = max(1, min(num_flashcards, 15))
        pool = StudyMaterialGenerator._flashcard_pool(topic, difficulty)

        if num_flashcards <= len(pool):
            selected = random.sample(pool, num_flashcards)
        else:
            selected = pool[:]
            while len(selected) < num_flashcards:
                selected.append(random.choice(pool))
            random.shuffle(selected)
            selected = selected[:num_flashcards]

        flashcards = []

        for index, card in enumerate(selected, start=1):
            flashcards.append(
                {
                    "id": index,
                    "question": card.get("question", ""),
                    "answer": card.get("answer", ""),
                }
            )

        return flashcards

    @staticmethod
    def _quiz_pool(topic, difficulty="Beginner"):
        data = _knowledge(topic)
        display = data["display"]
        difficulty = _difficulty_label(difficulty)

        pool = [
            {
                "question": f"Which option best describes {display}?",
                "correct_answer": data["definition"],
                "wrong_answers": [
                    f"{display} is only a random fact to memorize.",
                    f"{display} has no connection to real learning.",
                    f"{display} is mainly about ignoring examples.",
                ],
            }
        ]

        for fact in data["important_facts"]:
            pool.append(
                {
                    "question": f"Which statement about {display} is correct?",
                    "correct_answer": fact,
                    "wrong_answers": [
                        random.choice(data["common_mistakes"]),
                        f"{display} is not connected to any key terms.",
                        f"{display} should only be memorized without understanding.",
                    ],
                }
            )

        for term in data["key_terms"]:
            other_terms = [t for t in data["key_terms"] if t != term]
            wrongs = other_terms[:]

            while len(wrongs) < 3:
                wrongs.append(random.choice(["unrelated idea", "random fact", "incorrect term", "minor detail"]))

            pool.append(
                {
                    "question": f"Which key term is strongly connected to {display}?",
                    "correct_answer": term,
                    "wrong_answers": wrongs,
                }
            )

        for example in data["examples"]:
            pool.append(
                {
                    "question": f"Which example is related to {display}?",
                    "correct_answer": example,
                    "wrong_answers": [
                        f"An example that ignores the meaning of {display}.",
                        f"A situation with no connection to {display}.",
                        "A random unrelated classroom activity.",
                    ],
                }
            )

        if difficulty in ["Intermediate", "Advanced"]:
            pool.extend(
                [
                    {
                        "question": f"What is a common mistake when learning {display}?",
                        "correct_answer": random.choice(data["common_mistakes"]),
                        "wrong_answers": [
                            f"Using examples to understand {display}.",
                            f"Reviewing key terms for {display}.",
                            f"Practicing recall about {display}.",
                        ],
                    },
                    {
                        "question": f"Why can {display} be useful outside memorization?",
                        "correct_answer": random.choice(data["real_world_use"]),
                        "wrong_answers": [
                            f"It has no real-world connection.",
                            f"It is useful only if you never practice it.",
                            f"It should not be connected to examples.",
                        ],
                    },
                    {
                        "question": f"What is a good study strategy for {display}?",
                        "correct_answer": f"Explain {display} in your own words and test yourself with questions.",
                        "wrong_answers": [
                            "Only reread notes without testing yourself.",
                            "Skip examples completely.",
                            "Memorize words without understanding meaning.",
                        ],
                    },
                ]
            )

        if difficulty == "Advanced":
            pool.extend(
                [
                    {
                        "question": f"What shows deeper understanding of {display}?",
                        "correct_answer": f"Connecting facts, examples, mistakes, and real-world uses of {display}.",
                        "wrong_answers": [
                            f"Only repeating the word {display}.",
                            "Avoiding all examples.",
                            "Ignoring common misconceptions.",
                        ],
                    },
                    {
                        "question": f"How should an advanced learner approach {display}?",
                        "correct_answer": f"Compare ideas, question misconceptions, and apply {display} to real situations.",
                        "wrong_answers": [
                            "Only memorize the title.",
                            "Never connect it to examples.",
                            "Avoid explaining it to others.",
                        ],
                    },
                ]
            )

        random.shuffle(pool)
        return pool

    @staticmethod
    def generate_quiz(topic, difficulty="Beginner", num_questions=5):
        try:
            num_questions = int(num_questions)
        except Exception:
            num_questions = 5

        num_questions = max(1, min(num_questions, 15))
        pool = StudyMaterialGenerator._quiz_pool(topic, difficulty)

        selected = random.sample(pool, min(num_questions, len(pool)))
        quiz = []

        for index, item in enumerate(selected, start=1):
            correct = item["correct_answer"]
            options = _shuffle_options(correct, item.get("wrong_answers", []))

            quiz.append(
                {
                    "id": index,
                    "question": item["question"],
                    "options": options,
                    "correct_answer": correct,
                }
            )

        return quiz

    @staticmethod
    def generate_all_materials(topic, difficulty="Beginner", num_flashcards=5, num_questions=5, **kwargs):
        if "flashcard_count" in kwargs:
            num_flashcards = kwargs["flashcard_count"]
        if "quiz_count" in kwargs:
            num_questions = kwargs["quiz_count"]
        if "num_quiz_questions" in kwargs:
            num_questions = kwargs["num_quiz_questions"]

        explanation = StudyMaterialGenerator.generate_explanation(topic, difficulty)
        key_points = StudyMaterialGenerator.generate_key_points(topic, difficulty)
        flashcards = StudyMaterialGenerator.generate_flashcards(topic, difficulty, num_flashcards)
        quiz = StudyMaterialGenerator.generate_quiz(topic, difficulty, num_questions)

        notes = f"""
StudyMate AI Notes

Topic: {_display_topic(topic)}
Difficulty: {difficulty}

Explanation:
{explanation}

Key Points:
{chr(10).join("- " + point for point in key_points)}

Flashcards:
{chr(10).join(str(card["id"]) + ". Q: " + card["question"] + " | A: " + card["answer"] for card in flashcards)}

Quiz Questions:
{chr(10).join(str(question["id"]) + ". " + question["question"] + " | Correct Answer: " + question["correct_answer"] for question in quiz)}
"""

        return {
            "topic": _display_topic(topic),
            "difficulty": difficulty,
            "explanation": explanation,
            "key_points": key_points,
            "flashcards": flashcards,
            "quiz": quiz,
            "quiz_questions": quiz,
            "notes": notes,
            "study_notes": notes,
            "summary": explanation,
        }


def generate_explanation(topic, difficulty="Beginner"):
    return StudyMaterialGenerator.generate_explanation(topic, difficulty)


def generate_key_points(topic, difficulty="Beginner"):
    return StudyMaterialGenerator.generate_key_points(topic, difficulty)


def generate_flashcards(topic, difficulty="Beginner", num_flashcards=5):
    return StudyMaterialGenerator.generate_flashcards(topic, difficulty, num_flashcards)


def generate_quiz(topic, difficulty="Beginner", num_questions=5):
    return StudyMaterialGenerator.generate_quiz(topic, difficulty, num_questions)


def generate_all_materials(topic, difficulty="Beginner", num_flashcards=5, num_questions=5, **kwargs):
    return StudyMaterialGenerator.generate_all_materials(
        topic,
        difficulty,
        num_flashcards,
        num_questions,
        **kwargs,
    )