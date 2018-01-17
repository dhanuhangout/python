'''Build configuration file of problems in maths.'''

py_binary(
    name="hcf_using_euclids_theorem",
    srcs=["hcf_using_euclids_theorem.py"],
    main="hcf_using_euclids_theorem.py",
)

py_binary(
    name="matrices",
    srcs=["matrices.py"],
    main="matrices.py",
)

py_binary(
    name="number_system_conversion",
    srcs=["number_system.py"],
    main="number_system.py",
)

py_test(
    name="number_system_conversion_test",
    srcs=["number_system_test.py"],
    deps = [":number_system_conversion"],
    main="number_system_test.py",
    size="small",
)