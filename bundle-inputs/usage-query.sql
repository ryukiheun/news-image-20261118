-- Usage rows for the build (d3758f9c) and fix (951d2f31) subagent sessions
-- of news-image-20261118. Rows appear only AFTER each session ends.
-- Parent session 1de10b8f-1185-4ebf-8021-73ffc068891b predates the
-- competition opening and is NOT bundled (bundle with --no-discover
-- --session <each session> only).
-- The 3 egm-review sessions only read the entry and wrote no entry code;
-- they are not bundled (only sessions that worked on the entry are).
SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, u.created_at AS created_at FROM agent.agent_message_token_usage u WHERE u.agent_id IN ('d3758f9c-6a02-4a2e-8f04-22866b33dcf7', '951d2f31-4c2e-4693-805b-6c434f662ec5') ORDER BY u.created_at ASC
