fights_table_insert_query = """
                                INSERT INTO fights
                                    (
                                    event_id, fighter_rc, fighter_bc, fight_winner, 
                                    weight_class, method, ending_round, ending_time, 
                                    time_format, referee, details
                                    )
                                VALUES
                                    (
                                    %s, %s, %s, %s,
                                    %s, %s, %s, %s,
                                    %s, %s, %s
                                    )
                            """

fighters_table_insert_query = """
                                INSERT INTO fighters
                                    (
                                    name, nickname, height, reach, 
                                    stance, dob, slpm, str_acc, 
                                    sapm, str_def, td_avg, td_def, 
                                    sub_avg
                                    )
                                VALUES
                                    (
                                    %s, %s, %s, %s,
                                    %s, %s, %s, %s,
                                    %s, %s, %s, %s,
                                    %s
                                    )
                            """
events_table_insert_query = """
                                INSERT INTO events
                                    (
                                    id, name, date, location
                                    )
                                VALUES
                                    (
                                    %s, %s, %s, %s
                                    )"""

fight_total_summ_stats_raw_table_insert_query = """
                                                INSERT INTO fight_total_summ_stats_raw
                                                    (
                                                    fight_id,
                                                    rc_knockdowns, bc_knockdowns,
                                                    rc_sig_strks, bc_sig_strks,
                                                    rc_sig_strks_pct, bc_sig_strks_pct, 
                                                    rc_total_strks, bc_total_strks, 
                                                    rc_takedowns, bc_takedowns, 
                                                    rc_takedown_pct, bc_takedown_pct, 
                                                    rc_sub_attempts, bc_sub_attempts,
                                                    rc_reversals, bc_reversals,
                                                    rc_grnd_ctrl, bc_grnd_ctrl
                                                    )
                                                VALUES 
                                                    (
                                                    %s, %s, %s,
                                                    %s, %s, %s, %s,
                                                    %s, %s, %s, %s,
                                                    %s, %s, %s, %s,
                                                    %s, %s, %s, %s
                                                    )
                                            """

fight_sig_strks_summ_stats_raw_table_insert_query = """
                                                    INSERT INTO fight_sig_strks_summ_stats_raw
                                                        (
                                                        fight_id,
                                                        rc_sig_strks, bc_sig_strks, 
                                                        rc_sig_strks_pct, bc_sig_strks_pct,
                                                        rc_head, bc_head, 
                                                        rc_body, bc_body,
                                                        rc_leg, bc_leg, 
                                                        rc_distance, bc_distance,
                                                        rc_clinch, bc_clinch, 
                                                        rc_grnd, bc_grnd,
                                                        rc_head_lbt_pct, bc_head_lbt_pct, 
                                                        rc_body_lbt_pct, bc_body_lbt_pct,
                                                        rc_leg_lbt_pct, bc_leg_lbt_pct, 
                                                        rc_distance_lbt_pct, bc_distance_lbt_pct,
                                                        rc_clinch_lbt_pct, bc_clinch_lbt_pct, 
                                                        rc_grnd_lbt_pct, bc_grnd_lbt_pct
                                                        )
                                                    VALUES
                                                        (
                                                        %s, 
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s
                                                        )
                                                """

fight_rbr_stats_raw_table_insert_query = """
                                        INSERT INTO fight_rbr_stats_raw
                                            (
                                            fight_id, round, 
                                            rc_knockdowns, bc_knockdowns, 
                                            rc_sig_strks, bc_sig_strks,
                                            rc_sig_strks_pct, bc_sig_strks_pct,
                                            rc_total_strks, bc_total_strks,
                                            rc_takedowns, bc_takedowns,
                                            rc_takedown_pct, bc_takedown_pct,
                                            rc_sub_att, bc_sub_att,
                                            rc_revs, bc_revs,
                                            rc_grnd_ctrl, bc_grnd_ctrl
                                            )
                                        VALUES
                                            (
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s
                                            )
                                    """

fight_rbr_sig_strks_stats_raw_table_insert_query = """
                                                    INSERT INTO fight_rbr_sig_strks_stats_raw
                                                        (
                                                        fight_id, round,
                                                        rc_sig_strks, bc_sig_strks,
                                                        rc_sig_strks_pct, bc_sig_strks_pct,
                                                        rc_head, bc_head,
                                                        rc_body, bc_body, 
                                                        rc_leg, bc_leg,
                                                        rc_distance, bc_distance,
                                                        rc_clinch, bc_clinch, 
                                                        rc_grnd, bc_grnd
                                                        )
                                                    VALUES
                                                        (
                                                        %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s,
                                                        %s, %s, %s, %s
                                                        )
                                                """
