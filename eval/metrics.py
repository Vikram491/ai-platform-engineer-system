import json
import time

from pipeline.intent import extract_intent
from pipeline.design import design_system
from pipeline.schema import generate_schema
from pipeline.refine import refine_output

from validator.validator import validate_all
from validator.repair import repair

from runtime.simulator import simulate_execution


def run_evaluation():

    # -----------------------------------
    # Load Dataset
    # -----------------------------------

    with open("eval/dataset.json", "r") as file:

        dataset = json.load(file)

    # -----------------------------------
    # Metrics
    # -----------------------------------

    total = len(dataset)

    success_count = 0

    repair_count = 0

    failure_count = 0

    total_latency = 0

    failure_types = {}

    # -----------------------------------
    # Run Tests
    # -----------------------------------

    for item in dataset:

        prompt = item["prompt"]

        print("\n===================================")
        print("PROMPT:", prompt)

        start_time = time.time()

        try:

            # -----------------------------------
            # Pipeline
            # -----------------------------------

            intent = extract_intent(prompt)

            design = design_system(intent)

            schema = generate_schema(design)

            refined = refine_output(schema)

            # -----------------------------------
            # Validation
            # -----------------------------------

            valid, errors = validate_all(refined)

            # -----------------------------------
            # Repair
            # -----------------------------------

            if not valid:

                repair_count += 1

                refined = repair(refined, errors)

                valid, errors = validate_all(refined)

            # -----------------------------------
            # Runtime Simulation
            # -----------------------------------

            runtime_report = simulate_execution(refined)

            # -----------------------------------
            # Success Tracking
            # -----------------------------------

            if valid and runtime_report["runtime_ready"]:

                success_count += 1

                print("STATUS: SUCCESS")

            else:

                failure_count += 1

                print("STATUS: FAILED")

                for error in errors:

                    if error not in failure_types:

                        failure_types[error] = 0

                    failure_types[error] += 1

            # -----------------------------------
            # Latency
            # -----------------------------------

            latency = time.time() - start_time

            total_latency += latency

            print(f"LATENCY: {latency:.2f} seconds")

        except Exception as e:

            failure_count += 1

            print("CRASH:", str(e))

    # -----------------------------------
    # Final Metrics
    # -----------------------------------

    print("\n===================================")
    print("FINAL EVALUATION REPORT")
    print("===================================")

    print(f"Total Tests: {total}")

    print(f"Success Count: {success_count}")

    print(f"Failure Count: {failure_count}")

    print(f"Repair Activations: {repair_count}")

    print(f"Success Rate: {(success_count / total) * 100:.2f}%")

    print(f"Average Latency: {(total_latency / total):.2f} sec")

    print("\nFailure Types:")

    for key, value in failure_types.items():

        print(f"{key}: {value}")