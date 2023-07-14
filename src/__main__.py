# scv/__main__.py
import argparse

from src.helpers.constants import Constants


def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description="Data Pipeline Job starter script " "Starts all the Data Pipeline entities jobs.",
        epilog="From Aditya Chouhan",
    )

    parser.add_argument("table_name", help="table name from the stream which needs to be loaded")

    parser.add_argument("load_type", help="load type of the job (FULL/INCREMENTAL)")

    args = parser.parse_args()
    print(args)

    if args.load_type != Constants().LOAD_TYPE_FULL and args.load_type != Constants().LOAD_TYPE_INCR:
        raise Exception(f"Given load type {args.load_type} doesn't exist!")

    import src.app_main as app_main

    if args.table_name in [
        Constants().TB_SF_DEVELOPER_DTL,
        Constants().TB_SF_DEVOPS_DTL,
        Constants().TB_SF_TESTER_DTL,
    ]:
        app_main.DataPipelineMain(args.table_name, args.load_type).run_data_pipeline_process()


if __name__ == "__main__":
    main()
