"""In this exercise, we'll develop a simple control system for a nuclear reactor.

For a reactor to produce the power it must be in a state of criticality. If the reactor is in a state less than criticality, it can become damaged. If the reactor state goes beyond criticality, it can overload and result in a meltdown. We want to mitigate the chances of meltdown and correctly manage reactor state.

The following three tasks are all related to writing code for maintaining ideal reactor state.

Task 1

The first thing a control system has to do is check if the reactor is balanced in criticality. A reactor is said to be critical if it satisfies the following conditions:

The temperature is less than 800 K.
The number of neutrons emitted per second is greater than 500.
The product of temperature and neutrons emitted per second is less than 500000.
Implement the function is_criticality_balanced() that takes temperature measured in kelvin and neutrons_emitted as parameters, and returns True if the criticality conditions are met, False if not.

>>> is_criticality_balanced(750, 600)
True

Task 2

Once the reactor has started producing power its efficiency needs to be determined. Efficiency can be grouped into 4 bands:

green -> efficiency of 80% or more,
orange -> efficiency of less than 80% but at least 60%,
red -> efficiency below 60%, but still 30% or more,
black -> less than 30% efficient.
The percentage value can be calculated as (generated_power/theoretical_max_power)*100 where generated_power = voltage * current. Note that the percentage value is usually not an integer number, so make sure to consider the proper use of the < and <= comparisons.

Implement the function reactor_efficiency(<voltage>, <current>, <theoretical_max_power>), with three parameters: voltage, current, and theoretical_max_power. This function should return the efficiency band of the reactor : 'green', 'orange', 'red', or 'black'.

>>> reactor_efficiency(200,50,15000)
'orange'

Task 3

Your final task involves creating a fail-safe mechanism to avoid overload and meltdown. This mechanism will determine if the reactor is below, at, or above the ideal criticality threshold. Criticality can then be increased, decreased, or stopped by inserting (or removing) control rods into the reactor.

Implement the function called fail_safe(), which takes 3 parameters: temperature measured in kelvin, neutrons_produced_per_second, and threshold, and outputs a status code for the reactor.

If temperature * neutrons_produced_per_second < 90% of threshold, output a status code of 'LOW' indicating that control rods must be removed to produce power.

If the value temperature * neutrons_produced_per_second is within 10% of the threshold (so either 0-10% less than the threshold, at the threshold, or 0-10% greater than the threshold), the reactor is in criticality and the status code of 'NORMAL' should be output, indicating that the reactor is in optimum condition and control rods are in an ideal position.

If temperature * neutrons_produced_per_second is not in the above-stated ranges, the reactor is going into meltdown and a status code of 'DANGER' must be passed to immediately shut down the reactor.

>>> fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
'DANGER'
"""

# My solution
"""
Exercism solution for "Meltdown Mitigation"
"""
def is_criticality_balanced(temperature: int, neutrons_emitted: int) -> bool:
    """
 
    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not
 
    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500_000
    )
def reactor_efficiency(voltage: int, current: int, theoretical_max_power: int) -> str:
    """
 
    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'
 
    Efficiency can be grouped into 4 bands:
 
    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient
 
    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    efficiency = voltage * current / theoretical_max_power * 100
    if efficiency >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"
    return "black"
def fail_safe(
    temperature: int, neutrons_produced_per_second: int, threshold: int
) -> str:
    """
 
    :param temperature: int
    :param neutrons_produced_per_second: int
    :param threshold: int
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'
 
    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """
    if temperature * neutrons_produced_per_second < 0.9 * threshold:
        return 'LOW'
    if (temperature * neutrons_produced_per_second >= 0.9 * threshold and
          temperature * neutrons_produced_per_second <= 1.1 * threshold):
        return 'NORMAL'
    return 'DANGER'