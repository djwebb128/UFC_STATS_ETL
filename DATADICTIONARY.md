# Data Dictionary
## Events 
| Column Name | Data Type | Description                        |
| ----------- | --------- | ---------------------------------- |
| id          | SERIAL    | Unique identifier for each event.  |
| name        | text      | Name of the event (e.g., UFC 2: No Way Out). |
| date        | date      | Date of the event.                 |
| location    | text      | Location or venue of the event.    |

## Fights
| Column Name  | Data Type  | Description                                   |
| ------------ | ---------- | --------------------------------------------- |
| id           | SERIAL     | Unique identifier for each fight.             |
| event_id     | int4       | Foreign key referencing `events.id`.          |
| fighter_rc   | text       | Fighter in red corner.                        |
| fighter_bc   | text       | Fighter in blue corner.                       |
| fight_winner | text       | Winner of the fight.                          |
| weight_class | text       | Weight class of the fight.                    |
| method       | text       | Method of victory (KO, Submission, Decision). |
| ending_round | int2       | Round when the fight ended.                   |
| ending_time  | time       | Time in the round when the fight ended.       |
| time_format  | text       | Format of the fight duration.                 |
| referee      | text       | Referee of the fight.                         |
| details      | text[3][2] | Nested array containing detailed fight info.  |

## Fighters
| Column Name | Data Type    | Description                                         |
| ----------- | ------------ | --------------------------------------------------- |
| id          | SERIAL       | Unique identifier for each fighter.                 |
| name        | text         | Full name of the fighter.                           |
| nickname    | text         | Fighter’s nickname or alias.                        |
| height      | text         | Height of the fighter.                              |
| reach       | int4         | Fighter’s reach (unit to confirm).                  |
| stance      | text         | Primary fighting stance (e.g., Orthodox, Southpaw). |
| dob         | date         | Date of birth of the fighter.                       |
| slpm        | numeric(4,2) | Significant strikes landed per minute.              |
| str_acc     | int2         | Striking accuracy percentage.                       |
| sapm        | numeric(4,2) | Significant strikes absorbed per minute.            |
| str_def     | int2         | Striking defense percentage.                        |
| td_avg      | numeric(3,2) | Average takedowns per 15 minutes.                   |
| td_def      | int2         | Takedown defense percentage.                        |
| sub_avg     | numeric(3,2) | Average submissions per 15 minutes.                 |


## Fight Total Summary Statistics 
| Column Name      | Data Type | Description                                |
| ---------------- | --------- | ------------------------------------------ |
| fight_id         | int4      | Foreign key referencing `fights.id`.       |
| rc_knockdowns    | int2      | Knockdowns by red corner.                  |
| bc_knockdowns    | int2      | Knockdowns by blue corner.                 |
| rc_sig_strks     | text      | Significant strikes by red corner.         |
| bc_sig_strks     | text      | Significant strikes by blue corner.        |
| rc_sig_strks_pct | int2      | Significant strike accuracy (red corner).  |
| bc_sig_strks_pct | int2      | Significant strike accuracy (blue corner). |
| rc_total_strks   | text      | Total strikes by red corner.               |
| bc_total_strks   | text      | Total strikes by blue corner.              |
| rc_takedowns     | text      | Takedowns attempted by red corner.         |
| bc_takedowns     | text      | Takedowns attempted by blue corner.        |
| rc_takedown_pct  | int2      | Takedown accuracy (red corner).            |
| bc_takedown_pct  | int2      | Takedown accuracy (blue corner).           |
| rc_sub_attempts  | int2      | Submission attempts (red corner).          |
| bc_sub_attempts  | int2      | Submission attempts (blue corner).         |
| rc_reversals     | int2      | Reversals (red corner).                    |
| bc_reversals     | int2      | Reversals (blue corner).                   |
| rc_grnd_ctrl     | time      | Ground control time (red corner).          |
| bc_grnd_ctrl     | time      | Ground control time (blue corner).         |


## Fight Round by Round Statistics
| Column Name      | Data Type | Description                          |
| ---------------- | --------- | ------------------------------------ |
| fight_id         | int4      | Foreign key referencing `fights.id`. |
| round            | int2      | Round number.                        |
| rc_knockdowns    | int2      | Knockdowns by red corner.            |
| bc_knockdowns    | int2      | Knockdowns by blue corner.           |
| rc_sig_strks     | text      | Significant strikes (red corner).    |
| bc_sig_strks     | text      | Significant strikes (blue corner).   |
| rc_sig_strks_pct | int2      | Strike accuracy (red corner).        |
| bc_sig_strks_pct | int2      | Strike accuracy (blue corner).       |
| rc_total_strks   | text      | Total strikes (red corner).          |
| bc_total_strks   | text      | Total strikes (blue corner).         |
| rc_takedowns     | text      | Takedowns (red corner).              |
| bc_takedowns     | text      | Takedowns (blue corner).             |
| rc_takedown_pct  | int2      | Takedown accuracy (red corner).      |
| bc_takedown_pct  | int2      | Takedown accuracy (blue corner).     |
| rc_sub_att       | int2      | Submission attempts (red corner).    |
| bc_sub_att       | int2      | Submission attempts (blue corner).   |
| rc_revs          | int2      | Reversals (red corner).              |
| bc_revs          | int2      | Reversals (blue corner).             |
| rc_grnd_ctrl     | time      | Ground control time (red corner).    |
| bc_grnd_ctrl     | time      | Ground control time (blue corner).   |


## Fight Significant Strikes Summary Statistics
| Column Name         | Data Type | Description                                |
| ------------------- | --------- | ------------------------------------------ |
| fight_id            | int4      | Foreign key referencing `fights.id`.       |
| rc_sig_strks        | text      | Significant strikes by red corner.         |
| bc_sig_strks        | text      | Significant strikes by blue corner.        |
| rc_sig_strks_pct    | int2      | Significant strike accuracy (red corner).  |
| bc_sig_strks_pct    | int2      | Significant strike accuracy (blue corner). |
| rc_head             | text      | Head strikes by red corner.                |
| bc_head             | text      | Head strikes by blue corner.               |
| rc_body             | text      | Body strikes by red corner.                |
| bc_body             | text      | Body strikes by blue corner.               |
| rc_leg              | text      | Leg strikes by red corner.                 |
| bc_leg              | text      | Leg strikes by blue corner.                |
| rc_distance         | text      | Distance strikes by red corner.            |
| bc_distance         | text      | Distance strikes by blue corner.           |
| rc_clinch           | text      | Clinch strikes by red corner.              |
| bc_clinch           | text      | Clinch strikes by blue corner.             |
| rc_grnd             | text      | Ground strikes by red corner.              |
| bc_grnd             | text      | Ground strikes by blue corner.             |
| rc_head_lbt_pct     | int2      | Head strike landing % (red corner).        |
| bc_head_lbt_pct     | int2      | Head strike landing % (blue corner).       |
| rc_body_lbt_pct     | int2      | Body strike landing % (red corner).        |
| bc_body_lbt_pct     | int2      | Body strike landing % (blue corner).       |
| rc_leg_lbt_pct      | int2      | Leg strike landing % (red corner).         |
| bc_leg_lbt_pct      | int2      | Leg strike landing % (blue corner).        |
| rc_distance_lbt_pct | int2      | Distance strike landing % (red corner).    |
| bc_distance_lbt_pct | int2      | Distance strike landing % (blue corner).   |
| rc_clinch_lbt_pct   | int2      | Clinch strike landing % (red corner).      |
| bc_clinch_lbt_pct   | int2      | Clinch strike landing % (blue corner).     |
| rc_grnd_lbt_pct     | int2      | Ground strike landing % (red corner).      |
| bc_grnd_lbt_pct     | int2      | Ground strike landing % (blue corner).     |


## Fight Round by Round Significant Strikes Summary Statistics
| Column Name      | Data Type | Description                          |
| ---------------- | --------- | ------------------------------------ |
| fight_id         | int4      | Foreign key referencing `fights.id`. |
| round            | int2      | Round number.                        |
| rc_sig_strks     | text      | Significant strikes (red corner).    |
| bc_sig_strks     | text      | Significant strikes (blue corner).   |
| rc_sig_strks_pct | int2      | Strike accuracy (red corner).        |
| bc_sig_strks_pct | int2      | Strike accuracy (blue corner).       |
| rc_head          | text      | Head strikes (red corner).           |
| bc_head          | text      | Head strikes (blue corner).          |
| rc_body          | text      | Body strikes (red corner).           |
| bc_body          | text      | Body strikes (blue corner).          |
| rc_leg           | text      | Leg strikes (red corner).            |
| bc_leg           | text      | Leg strikes (blue corner).           |
| rc_distance      | text      | Distance strikes (red corner).       |
| bc_distance      | text      | Distance strikes (blue corner).      |
| rc_clinch        | text      | Clinch strikes (red corner).         |
| bc_clinch        | text      | Clinch strikes (blue corner).        |
| rc_grnd          | text      | Ground strikes (red corner).         |
| bc_grnd          | text      | Ground strikes (blue corner).        |
